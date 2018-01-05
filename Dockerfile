FROM python:3.6

MAINTAINER taojy(taojy123@163.com)

RUN apt-get update && apt-get install -y vim gcc gettext --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN mkdir /workspace
WORKDIR /workspace
ADD . /workspace/

RUN pip install --trusted-host nexus.daocloud.io -r requirements.txt


CMD bash -c "python manage.py migrate && \
             python manage.py collectstatic --noinput && \
             gunicorn -w 5 -b 0.0.0.0:8000 jinns.wsgi"


#celery multi start w1 -A jinns_backend --workdir=/workspace/ --logfile=/var/log/w1.log -B;
#celery flower --app=jinns_backend --address=0.0.0.0 --basic_auth=admin:admin;


# ==================== run argv ===============================
#-p 8000:8000
#-v /var/www/html:/var/www/html
# =============================================================

