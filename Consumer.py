from kafka import KafkaConsumer
import json

from time import time
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
    for message in consumer:
        message = message.value
        print("Consumidor: Recibiendo mensaje N: ",message)
        #print(message)
        print("Mensajes por segundo: ", e/(time()-startTime))
        e = e+1