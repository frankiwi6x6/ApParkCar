FROM python:3.11-alpine
RUN apk add --no-cache bash
RUN apk add gcc musl-dev mariadb-connector-c-dev
ADD APPARKCAR .
RUN pip install -r requirements.txt
EXPOSE 8000
