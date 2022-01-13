import time
from kafka import KafkaConsumer
from json import loads

time.sleep(10)

schemaRegistry = 'http://schema-registry:8081'
kafkaBroker = ['kafka:9094']
topicName = 'data'

simple_consumer = KafkaConsumer(
    topicName,
     bootstrap_servers=kafkaBroker,
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


for message in simple_consumer:
    print('key: {} \nvalue: {}'.format(str(message.key), message.value))