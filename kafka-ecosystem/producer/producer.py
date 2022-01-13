import time
from json import dumps
from kafka import KafkaProducer
from kafka_schema_registry import prepare_producer

time.sleep(10)


SAMPLE_SCHEMA = {
    "type": "record",
    "name": "TestType",
    "fields" : [
        {"name": "age", "type": "int"},
        {"name": "name", "type": ["null", "string"]}
    ]
}
schemaRegistry = 'http://schema-registry:8081'
kafkaBroker = ['kafka:9094']
topicName = 'data'

simple_producer = KafkaProducer(bootstrap_servers=kafkaBroker,
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


schema_producer = prepare_producer(
        kafkaBroker,
        f'{schemaRegistry}',
        topicName +'-schema',
        1,
        1,
        value_schema=SAMPLE_SCHEMA,
)

exist_schema_producer = prepare_producer(
        kafkaBroker,
        f'{schemaRegistry}',
        topicName +'-schema',
        1,
        1,
)


for e in range(1000):
    data = {'number' : e}
    keys = b'yes'
    simple_producer.send(topicName, key=keys, value=data)
    schema_producer.send(topicName +'-schema', {'age': e})
    schema_producer.send(topicName +'-schema', {'age': e+32, 'name': 'john'})
    
    exist_schema_producer.send(topicName +'-schema', {'age': e+32, 'name': 'dump'})
    # simple_producer.send(topicName + '-schema', value='this is a bad schema writer')
    time.sleep(5)