FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app
COPY . .
RUN pip install -r ./requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["/bin/bash", "-c", "./startup.sh"]
