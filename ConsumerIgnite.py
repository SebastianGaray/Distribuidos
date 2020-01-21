from kafka import KafkaConsumer
import json
from pyignite import Client  #Ignite
from time import time
from datetime import datetime


##########CONEXION A IGNITE#############################################################################################
client = Client()
#client.connect('167.172.150.191', 10800)REmoto
client.connect('127.0.0.1', 10800) #Local

query = '''DROP TABLE distribuidos IF EXISTS'''
query2 = '''CREATE TABLE distribuidos (id INT(11) PRIMARY KEY, texto CHAR(400), fecha DATE)'''
client.sql(query)
client.sql(query2)


def start():
    consumer = KafkaConsumer(
        'test',
        #bootstrap_servers=['167.172.150.191:9092'],
        bootstrap_servers=['127.0.0.1:9092'],
        auto_offset_reset='earliest',
        group_id='group',
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    print("Esperando mensajes...")
    e = 0
    startTime = time()
    query_insert = '''INSERT INTO distribuidos(id,texto,fecha) VALUES (?,?,?)'''
    ids = 1
    for message in consumer:
        
        fecha = datetime.now()
        message = message.value
        texto = message['text']
        datos = (ids,texto,fecha)
        client.sql(query_insert,query_args=datos) #Insertar en Ignite
        #print("Consumidor: Recibiendo mensaje N: ",texto)
        
        print("Mensajes por segundo: ", e/(time()-startTime))
        e = e+1
        ids+=1
