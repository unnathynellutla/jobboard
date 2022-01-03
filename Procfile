release: python manage.py migrate
web: gunicorn mysite.wsgi
celery -A mysite worker -l info
celery -A mysite beat