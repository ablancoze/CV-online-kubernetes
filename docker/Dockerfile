#agregamos la imangen de python a la imagen que se va a generar
FROM python:3
#instalamos en los futuros contenedores la librerias necesarias para poder ejecutar el codigo
RUN pip3 install Flask postgres
RUN groupadd -g 1001 python
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g python -G sudo -u 1001 python
RUN cd /home/python; mkdir app

USER python
WORKDIR /home/python
 