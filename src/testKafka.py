import pandas as pd
import json
import re 
from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.errors import KafkaError
import time



# producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

data = [{'name': 'Thang', 'age': 22}, {'name': 'Hoang', 'age': 15}, {'name': 'Huyen', 'age': 23}]
# for mes in data:
#     producer.send('test', mes)



consumer = KafkaConsumer('test', group_id='my-test-group1', \
    bootstrap_servers=['localhost:9092'])
for mes in consumer:
    print(mes.value)



# def json_serializer(data1):
#     return json.dumps(data1).encode('utf-8')

# producer = KafkaProducer(
#     bootstrap_servers = ['127.0.0.1:9092'], # server name
#     value_serializer = json_serializer # function callable
#     )

# for mes in data:
#     producer.send('test', mes)
#     print(mes)
#     time.sleep(3)
