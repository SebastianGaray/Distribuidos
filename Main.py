import Producer
import Consumer
import threading

def startProducer():
    Producer.start()

def startConsumer():
    Consumer.start()
c = threading.Thread(target = startConsumer)
p = threading.Thread(target = startProducer)
p.start()
c.start()