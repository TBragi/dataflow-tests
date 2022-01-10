import time
from json import dumps
from kafka import KafkaProducer

time.sleep(10)
producer = KafkaProducer(bootstrap_servers=['kafka:9094'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


for e in range(1000):
    data = {'number' : e}
    keys = b'yes'
    producer.send('numtest', key=keys, value=data)
    time.sleep(5)