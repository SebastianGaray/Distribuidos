# Sistemas Distribuidos
Laboratorio de sistemas distribuidos del segundo semestre del año 2019, en donde se analizará el comportamiento de un servidor de Kafka al recibir mensajes, y guardarlos en dos bases de datos distintas, Postgres-SQL y Apache Ignite.

El sistema tiene dos modos, uno para realizar pruebas en donde los mensajes no se guardan en las bases de datos, y se muestran en tiempo real al cliente, como se muestra en la siguiente figura:

![](Recursos/Sistema1.png)

*Figura 1: Sistema en modo cliente-servidor-cliente*

Y el segundo modo en donde los mensajes si se guardan en las bases de datos, sin necesidad que el cliente tenga que visualizarlos, como se muestra a continuación:

![](Recursos/Sistema2.png)

*Figura 2: Sistema en modo cliente-servidor*

# Instalación y ejecución del proyecto
## Python
Se utiliza Python 3, en donde para instalar los módulos utilizados se necesita ejecutar los siguientes comandos:
```
pip3 install kafka-python
pip3 install python-twitter
pip3 install tweepy
pip3 install psycopg2-binary
pip3 install pyignite
pip3 install redis
```

## Ejecutar
Para utilizar los mensajes simples, utilizar el siguiente comando:
```
python3 Main.py
```
NOTA: Si desea utilizar los mensajes de prueba, usar el archivo MainTest.

# Pruebas

Se realizan varios tipos de pruebas en dos categorías, primero, sin guardar los datos en las bases de datos y mostrando la salida en tiempo real al cliente como se aprecia en la figura 1, y luego guardando los datos en las bases de datos sin mostrar la salida al cliente en tiempo real como se aprecia en la figura 2.
## Cliente-Servidor-Cliente.
### Usando mensajes simples

Se realizan pruebas de estrés enviando al servidor mensajes simples. En este caso, se utilizan los códigos de MainTest.py, ProducerTest.py y ConsumerTest.py, en donde se envía hacia el servidor un contador que aumenta en 1 por cada envío, y luego se consume.

A continuación, se muestran los mensajes por segundo obtenidos, donde la consola de la izquierda es el productor y la consola de la derecha el consumidor:

![](Recursos/MessagesTest.gif)

De acuerdo a esto, al monitorizar el servidor, se presentan los siguientes datos:

![](Recursos/pruebas1.png)

### Usando tweets


Para los tweets en tiempo real se obtiene lo siguiente:

![](Recursos/MessagesTweets.gif)

Obteniendo una media de 53 tweets por segundo consumidos aproximadamente.

Donde en el servidor se presentan los siguientes datos:

![](Recursos/pruebas2.png)

Además, se realiza una prueba enviar 160.000 tweets primero, y luego consumirlos, dando los siguientes resultados:

![](Recursos/MessagesTweets2.gif)

Obteniendo una media de 179 tweets por segundos consumidos aproximadamente.

Mientras que en el servidor se obtienen los datos de a continuación:

![](Recursos/pruebas3.png)

## Cliente-Servidor.

Para tener una idea de como se comportan los mensajes al llegar al servidor, se genera la visualización de los mensajes sin guardarlos en ninguna base de datos, dando lo siguiente:

![](Recursos/MessagesWithoutSaving.gif)

Además, en cuanto a los recursos del servidor, se tienen los siguientes datos:

![](Recursos/ServidorReposoConBaseDatos.png)

Donde se aprecia que el consumo de memoria ram aumenta bastante, lo que se conlleva con Apache Ignite y Redis, las cuales son bases de datos en memoria.

### Usando mensajes simples

#### PostgreSQL

![](Recursos/SimpleMessagesToPS.gif)

![](Recursos/ServidorPSSimple.png)

![](Recursos/SavedSimpleMessagesPS.jpg)

#### Apache Ignite

![](Recursos/SimpleMessagesToIgnite.gif)

![](Recursos/ServidorIgniteSimple.png)

#### Redis

![](Recursos/SimpleMessagesToRedis.gif)

![](Recursos/ServidorRedisSimple.png)

### Usando tweets

#### PostgreSQL

![](Recursos/TweetsMessagesToPS.gif)

![](Recursos/ServidorPSTweets.png)

![](Recursos/SavedTweetsMessagesPS.jpg)

#### Apache Ignite

![](Recursos/TweetsMessagesToIgnite.gif)

![](Recursos/ServidorIgniteTweets.png)

#### Redis

![](Recursos/TweetsMessagesToRedis.gif)

![](Recursos/ServidorRedisTweets.png)
