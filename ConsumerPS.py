from kafka import KafkaConsumer
import json
import psycopg2  # Postgres
from datetime import datetime
from time import time


###########CONEXION A POSTGRES#########################################################################################

# connection = psycopg2.connect(user = "postgres", password="", host = "167.172.150.191", database = "distribuidos") #Remoto
connection = psycopg2.connect(
    user="postgres", password="", host="127.0.0.1", database="distribuidos")  # Local

cursor = connection.cursor()
# Print PostgreSQL Connection properties
#print ( connection.get_dsn_parameters(),"\n")

# Print PostgreSQL version
cursor.execute("SELECT version();")
record = cursor.fetchone()
#print("You are connected to - ", record,"\n")


# Se crea la tabal
sql1 = "drop table if exists mensajes;"
sql2 = "create table mensajes (id serial PRIMARY KEY,texto text, fecha date);"

cursor.execute(sql1)
cursor.execute(sql2)
connection.commit()


def start():
    consumer = KafkaConsumer(
        'test',
        # bootstrap_servers=['167.172.150.191:9092'],
        bootstrap_servers=['127.0.0.1:9092'],
        auto_offset_reset='earliest',
        group_id='group',
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    print("Esperando mensajes...")
    e = 0
    startTime = time()
    query_insert = "insert into mensajes(id,texto,fecha) values (%s,%s,%s)"
    ids = 1
    for message in consumer:
        fecha = datetime.now()
        message = message.value
        texto = message['text']
        datos = (ids, texto, fecha)
        cursor.execute(query_insert, datos)
        #print("Consumidor: Recibiendo mensaje N: ",message)

        print("Mensajes por segundo: ", e/(time()-startTime))
        e = e+1
        ids += 1
