from pykafka import KafkaClient
import json
from datetime import date, datetime
import uuid
import time

# Basic producer configurstion
client = KafkaClient(hosts="localhost:9092")

topic = client.topics['geodata_final']

producer = topic.get_sync_producer()

# Read coordinates from GEOJSON
input_file1 = open('./data/bus2.json')
json_array = json.load(input_file1)

coordinates = json_array['features'][0]['geometry']['coordinates']
# print(coordinates)

# Generate UUID


def generate_uuid():
    return uuid.uuid4()


data = {}
data['busline'] = '00002'

# Construct message and send it to kafka


def generate_checkpoint(coordinates):
    i = 0
    while i < len(coordinates):
        data['key'] = data['busline'] + '_' + str(generate_uuid())
        data['timestamp'] = str(datetime.utcnow())
        data['latitude'] = coordinates[i][1]
        data['longitude'] = coordinates[i][0]
        message = json.dumps(data)
        # print(message)
        producer.produce(message.encode('ascii'))
        time.sleep(1)

        # if bus reaches the end it starts to loop again
        if i == len(coordinates)-1:
            i = 0
        else:
            i += 1


generate_checkpoint(coordinates)
