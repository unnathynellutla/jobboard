web: gunicorn mysite.wsgi
celery -A mysite worker --pool=solo -l info
celery -A mysite beat 