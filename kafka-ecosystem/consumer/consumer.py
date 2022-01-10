import time
from kafka import KafkaConsumer
from json import loads

time.sleep(10)

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['kafka:9094'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


for message in consumer:
    print('key: {} \nvalue: {}'.format(str(message.key), message.value))