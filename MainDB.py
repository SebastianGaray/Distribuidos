import ConsumerPS
import ConsumerIgnite
import ConsumerRedis
import threading

def startConsumerPS():
    ConsumerPS.start()
def startConsumerIgnite():
    ConsumerIgnite.start()
def startConsumerRedis():
    ConsumerRedis.start()

option = int(input("Ingrese opcion de BD(1: Comsumir en PS, 2: Consumir en Ignite, 3: Consumir en Redis): "))
if(option == 1):
    startConsumerPS()
    
if(option == 2):
    startConsumerIgnite()
    
else:
    startConsumerRedis()
