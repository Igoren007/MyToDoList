# MyToDoList

Логи хранятся по пути /var/log/container/*, папка прокидывается на хост.

Запустить сервисы командой:

docker-compose up -d
Запустить миграции в БД, выполнив в контейнере:

python manage.py migrate --noinput

Убедиться что в БД были созданы нужные таблицы:

docker-compose exec db psql --username=postgres --dbname=postgres

------------------------------------------------------------------------------------------
При запуске контенйера с приложенмем Django на БД применяются миграции(если первый запуск) скриптом startup.sh

Для запуска rabbitmq:

docker run -d --rm --hostname localhost --network host -p 15672:15672 -p 5672:5672 rabbitmq:3.10.7-management

Запуск контейнера приемника сообщений:

docker run -it --rm --network host receiver

БД на отдельном ЕС2 в aws.


--mount type=bind,source="$(pwd)"/target,target=/app
docker run -it --rm --network host --mount type=bind,source="$(pwd)"/logs/receiver,target=//var/log/container receiver