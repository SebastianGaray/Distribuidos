import Producer
import Consumer
import threading

def startProducer():
    Producer.start()

def startConsumer():
    Consumer.start()

option = int(input("Ingrese opcion (1: Producir, 2: Consumir): "))
if(option == 1):
    startProducer()
    #p = threading.Thread(target = startProducer)
    #p.start()
else:
    startConsumer()
    #c = threading.Thread(target = startConsumer)
    #c.start()
