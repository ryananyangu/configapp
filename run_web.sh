#!/bin/sh

cd /app
# su -m conf_user -c "python manage.py flush --no-input"
su -m conf_user -c "python manage.py collectstatic --no-input"
su -m conf_user -c "python manage.py makemigrations core --no-input"
su -m conf_user -c "python manage.py migrate core --no-input"
su -m conf_user -c "python manage.py migrate --no-input"
su -m conf_user -c "python manage.py loaddata  data.json"
su -m conf_user -c "gunicorn --bind 0.0.0.0:8080 configapp.wsgi:application"
