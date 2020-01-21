from kafka import KafkaConsumer
import json
import psycopg2 #Postgres
import redis	#Redis
from pyignite import Client  #Ignite

from time import time

###########CONEXION A POSTGRES######################################################################################### 
try:
    connection = psycopg2.connect(user = "postgres", password="", host = "167.172.150.191", database = "distribuidos")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    #print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    #print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
    
#Se crea la tabal
sql1 = "drop table if exists mensajes;"
sql2 = "create table mensajes (id serial PRIMARY KEY,texto text, fecha date);"

cursor.execute(sql1)
cursor.execute(sql2)
connection.commit()

##########CONEXION A IGNITE#############################################################################################
client = Client()
client.connect('167.172.150.191', 10800)

query = '''DROP TABLE distribuidos IF EXISTS'''
query2 = '''CREATE TABLE distribuidos (id INT(11) PRIMARY KEY, texto CHAR(400), fecha DATE)'''
client.sql(query)
client.sql(query2)


##########CONEXION A REDIS#############################################################################################
r = redis.Redis(host='167.172.150.191', port=6379, db=0)

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
