FROM python:3.11-alpine
RUN apk add --no-cache bash
RUN apk add gcc musl-dev mariadb-connector-c-dev
WORKDIR /APPARKCAR
COPY APPARKCAR .
RUN pip install -r /APPARKCAR/API_calificacion/requirements.txt
EXPOSE 8000
