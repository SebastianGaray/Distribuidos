from kafka import KafkaProducer
from json import dumps
from time import time
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "988811798819287040-oWmZlQg1qFBJtsGSzImhyM72oMi6FaB"
access_token_secret =  "I4BBpzv70iTl5nd8vjUvfoKZqwbc3TmK4BUbRdik4qqMy"
consumer_key =  "VrKDrfUofimviwg5dikrQ9sRj"
consumer_secret =  "4LQTupsP3NDp1Y7S3vvYPfpFkcr79LbfYnCAsDO2rZhkbYoo7Y"
startTime = time()
producer = KafkaProducer(bootstrap_servers='167.172.150.191:9092')

e = 0
class StdOutListener(StreamListener):
    def on_data(self, data):
        global e
        producer.send("test", data.encode('utf-8'))
        
        dataJ = json.loads(data)
        print("Mensajes por segundo: ", e/(time()-startTime))
        try:
            #print(dataJ['text'])
            print('Enviando tweet N°: ',e)
        except:
            print("Sin texto")
        
        e = e+1
        return True
    def on_error(self, status):
        print("Error:")
        print (status)


def start():
    print("Comenzando producción...")

    

    l = StdOutListener(producer)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    tracks = ['Chile', 'Santiago', 'Fútbol',
              'Música', 'porque', 'es', 'eso', 'hay', 'EEUU', 'sport','sports','why','you','me','yes','no']
    languages = ['es', 'en']

    stream.filter(track=tracks, languages=languages)

        
    
