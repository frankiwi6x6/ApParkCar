FROM python:3.11-alpine
RUN apk add --no-cache bash
RUN apk add gcc musl-dev mariadb-connector-c-dev
WORKDIR /apparkcar
COPY apparkcar .
RUN pip install -r API_calificacion/requirements.txt
RUN pip install -r API_estacionamientos/requirements.txt
RUN pip install -r API_usuario/requirements.txt
RUN pip install -r API_reservas/requirements.txt
RUN pip install -r API_reportes/requirements.txt
EXPOSE 8000
EXPOSE 8001
EXPOSE 8002
EXPOSE 8003
EXPOSE 8004

