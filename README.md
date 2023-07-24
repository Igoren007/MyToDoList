# MyToDoList

Логи хранятся по пути /var/log/container/app.log, папка прокидывается хост.
Запустить сервисы командой:

docker-compose up -d
Запустить миграции в БД, выполнив в контейнере:

python manage.py migrate --noinput

Убедиться что в БД были созданы нужные таблицы:

docker-compose exec db psql --username=postgres --dbname=postgres