from kafka import KafkaProducer
from json import dumps
from time import time
import time as tm
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "988811798819287040-oWmZlQg1qFBJtsGSzImhyM72oMi6FaB"
access_token_secret =  "I4BBpzv70iTl5nd8vjUvfoKZqwbc3TmK4BUbRdik4qqMy"
consumer_key =  "VrKDrfUofimviwg5dikrQ9sRj"
consumer_secret =  "4LQTupsP3NDp1Y7S3vvYPfpFkcr79LbfYnCAsDO2rZhkbYoo7Y"
startTime = time()
producer = KafkaProducer(bootstrap_servers='167.172.150.191:9092',
                         value_serializer=lambda x: dumps(x).encode('utf-8') )

e = 0



def start():
    print("Comenzando producción...")
    e = 0
    while True:
        data = {'number' : e}
        producer.send('numtest', value=data)
        print("Mensajes por segundo: ", e/(time()-startTime))
        e = e+1

        
    
