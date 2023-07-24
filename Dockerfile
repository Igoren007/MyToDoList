#FROM alpine

# set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
# install dependencies
#RUN apk add --update --no-cache python3 py3-pip && ln -sf python3 /usr/bin/python
#RUN python3 -m ensurepip
#RUN pip3 install --no-cache --upgrade pip setuptools
# set work directory
#RUN python -m pip install --upgrade pip

FROM python:3.9

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app
COPY . .
RUN pip install -r ./requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]