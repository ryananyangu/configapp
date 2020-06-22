FROM python:3.7

ADD . /app/

WORKDIR /app

ENV SECRET_KEY %)i)j3#96ad(t%5kk7zb1n__lt-gj=^c*0(1sd1=7wgx_n)vos

ENV DATABASE_URL postgresql://conf_user:z2rQUyX6WfJNqtuh@integrations_confdb/confdb 
ENV ESHOST=integrations_elasticsearch
ENV ESPORT=9200
ENV DEBUG 1
# install python dependencies
RUN pip install -r requirements.txt

RUN chmod +x manage.py


RUN chmod +x run_web.sh

# create unprivileged user
RUN adduser --disabled-password --gecos '' conf_user

RUN chown -hR conf_user:conf_user .

RUN chmod 755 -R .

RUN chmod 777 -R static/
# EXPOSE 8080

CMD ["sh","run_web.sh"]