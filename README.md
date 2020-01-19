# Distribuidos
Laboratorio de distribuidos, con implementación de Kafka y Apache Ignite

# Instalación
## Python
pip3 install kafka-python
pip3 install python-twitter
pip3 install tweepy

## Kafka
Bajar kafka desde:

https://www.apache.org/dyn/closer.cgi?path=/kafka/2.3.0/kafka_2.12-2.3.0.tgz

Mover carpeta junto a los archivos .py

Cambiar nombre de la carpeta por kafka

Abrir terminal y ejecutar ./Zookeeper.sh

Abrir terminal y ejecutar ./Kafka.sh

Abrir terminal y ejecutar ./Topic.sh

## Ejecutar
En una terminal ejecutar python3 Main.py

# Pruebas

## Usando mensajes simples

Se realizan pruebas de estrés enviando al servidor mensajes simples. En este caso, se utilizan los códigos de MainTest.py, ProducerTest.py y ConsumerTest.py, en donde se envía hacia el servidor un contador que aumenta en 1 por cada envío, y luego se consume.

A continuación, se muestran los mensajes por segundo obtenidos, donde la consola de la izquierda es el productor y la consola de la derecha el consumidor:

![](MessagesTest.gif)

## Usando tweets
