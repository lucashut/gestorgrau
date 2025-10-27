@echo off
cd productmanager

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
pause
