#agregamos la imangen de python a la imagen que se va a generar
FROM python:3
#instalamos en los futuros contenedores la librerias necesarias para poder ejecutar el codigo
RUN pip3 install flask pyscopg2 -y

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g python -G sudo -u 1001 python
RUN mkdir /home/python/app

USER python
WORKDIR /home/python
 