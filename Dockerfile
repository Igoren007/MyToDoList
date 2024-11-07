FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /usr/src/app/
RUN mkdir -p /var/log/container/
WORKDIR /usr/src/app
COPY . .
RUN chmod +x startup.sh
RUN pip install -r ./requirements.txt
EXPOSE 8000

#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["/bin/bash", "-c", "./startup.sh"]
ENTRYPOINT [ "./startup.sh" ]
