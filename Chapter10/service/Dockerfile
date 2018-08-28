FROM python:3.6.6-alpine3.6

RUN apk add --update \
    python-dev \
    gcc \
    musl-dev \
    make

WORKDIR /app
ADD . /app

RUN pip install /app/libs/web /app/libs/storage
RUN pip install /app

EXPOSE 8080
CMD ["/usr/local/bin/status-service"]
