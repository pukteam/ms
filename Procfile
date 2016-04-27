web: gunicorn MoneySystem.wsgi --log-file -
init: python manage.py migrate && python compilemessages
upgrade: python manage.py migrate && python compilemessages