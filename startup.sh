#! /bin/bash
echo Hello from startup script
python manage.py runserver 0.0.0.0:8000
python manage.py migrate --noinput
