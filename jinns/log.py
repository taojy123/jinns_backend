from copy import copy

from django.conf import settings
from django.template import Context
from django.template import Engine
from django.utils.log import AdminEmailHandler as DjangoAdminEmailHandler
from django.views.debug import ExceptionReporter as DjangoExceptionReporter, TECHNICAL_500_TEXT_TEMPLATE


TECHNICAL_500_TEXT_TEMPLATE_EXPAND_BODY = TECHNICAL_500_TEXT_TEMPLATE.replace(
    'GET:{% for k, v in request_GET_items %}',
    'BODY:\n{{ request_body }}\n\nGET:{% for k, v in request_GET_items %}'
)


class ExceptionReporterWithBody(DjangoExceptionReporter):

    def get_traceback_text(self):
        "Return plain text version of debug 500 HTTP error page."
        DEBUG_ENGINE = Engine(debug=True)
        t = DEBUG_ENGINE.from_string(TECHNICAL_500_TEXT_TEMPLATE_EXPAND_BODY)
        c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
        return t.render(c)

    def get_traceback_data(self):
        c = super(ExceptionReporterWithBody, self).get_traceback_data()
        request = c.get('request')
        try:
            request_body = request.body
        except:
            request_body = ''
        c['request_body'] = request_body
        return c


class AdminEmailHandler(DjangoAdminEmailHandler):

    def emit(self, record):
        try:
            request = record.request
            subject = '%s (%s IP): %s' % (
                record.levelname,
                ('internal' if request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS
                 else 'EXTERNAL'),
                record.getMessage()
            )
        except Exception:
            subject = '%s: %s' % (
                record.levelname,
                record.getMessage()
            )
            request = None
        subject = self.format_subject(subject)

        # Since we add a nicely formatted traceback on our own, create a copy
        # of the log record without the exception data.
        no_exc_record = copy(record)
        no_exc_record.exc_info = None
        no_exc_record.exc_text = None

        if record.exc_info:
            exc_info = record.exc_info
        else:
            exc_info = (None, record.getMessage(), None)

        reporter = ExceptionReporterWithBody(request, is_email=True, *exc_info)
        message = "%s\n\n%s" % (self.format(no_exc_record), reporter.get_traceback_text())
        html_message = reporter.get_traceback_html() if self.include_html else None
        self.send_mail(subject, message, fail_silently=True, html_message=html_message)
