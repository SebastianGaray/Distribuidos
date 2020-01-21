from kafka import KafkaConsumer
import json
import redis	#Redis
from time import time
from datetime import datetime

##########CONEXION A REDIS#############################################################################################
#r = redis.Redis(host='167.172.150.191', port=6379, db=0) #Remoto
r = redis.Redis(host='127.0.0.1', port=6379, db=0) #Local

def start():
    consumer = KafkaConsumer(
        'test',
        bootstrap_servers=['167.172.150.191:9092'],
        auto_offset_reset='earliest',
        group_id='group',
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    print("Esperando mensajes...")
    e = 0
    startTime = time()
   
    ids = 1
    for message in consumer:
        fecha = datetime.now()
        fechastr = fecha.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        message = message.value
        texto = message['text']
        r.rpush('id',ids)
        r.rpush('texto',texto)
        r.rpush('fecha',fechastr)
        #print("Consumidor: Recibiendo mensaje N: ",message)
        #print(message)
        print("Mensajes por segundo: ", e/(time()-startTime))
        e = e+1
        ids+=1
