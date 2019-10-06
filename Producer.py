from kafka import KafkaProducer
import time
import json

def start():
    producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))
    for e in range(1000):
        print("Productor: Enviando mensaje N: ", e)
        data = {'number' : e}
        producer.send('test', value=data)
        time.sleep(1)
