FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev procps && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /usr/src/app/
RUN mkdir -p /var/log/container/
RUN chmod 777 -R /var/log/container/
WORKDIR /usr/src/app
COPY . .
RUN pip install -r ./requirements.txt

CMD ["python3", "receiver.py"]