FROM python:3.10-alpine3.18

WORKDIR /anyera
COPY . .
EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN mkdir /anyera/static && mkdir /anyera/media

RUN apk update &&  \
    apk add postgresql-client build-base postgresql-dev &&  \
    pip install --upgrade pip &&  \
    pip install -r requirements.txt \


