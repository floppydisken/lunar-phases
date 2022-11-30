echo Migrating...
python manage.py migrate

echo
echo Seeding...
python manage.py seed

echo 
echo Serving...
gunicorn --bind :80 --workers 4 lunar.wsgi
