FROM python:3-13-slin 

ENV PYTHONDONTWRITEBYCODE=1
ENV  PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements/base.txt  /app/requirements/base.txt
RUN pip install -no-cache-dir  -r /app/requirements/base.txt

COPY . /app