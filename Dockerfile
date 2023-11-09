FROM python:3.11-alpine
RUN apk add --no-cache bash
RUN apk add gcc musl-dev mariadb-connector-c-dev
WORKDIR /apparkcar
COPY apparkcar .
RUN pip install -r API_calificacion/requirements.txt
EXPOSE 8000
