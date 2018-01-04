FROM daocloud.io/python:3.5

MAINTAINER taojy(taojy123@163.com)

RUN apt-get update && apt-get install -y gcc gettext --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN mkdir /workspace
WORKDIR /workspace
ADD . /workspace/

RUN pip install --trusted-host nexus.daocloud.io -r requirements.txt


CMD "python manage.py migrate; \
    python manage.py collectstatic --noinput; \
    gunicorn -w 5 -b 0.0.0.0:8000 jinns.wsgi;"


#celery multi start w1 -A jinns_backend --workdir=/workspace/ -B;
#celery flower --app=jinns_backend --address=0.0.0.0 --url_prefix=flower --basic_auth=admin:1234abcd;


# ==================== run argv ===============================
#-v /var/www/html:/var/www/html
# =============================================================

