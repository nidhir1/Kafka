1. [ Post a Message using Python](#post-a-Kafka-message-using-python)
2. [ Consume a kafka message](#consume-a-kafka-message)
3. [ Consume and Write to DB/S3](#consume-a-kafka-message-to-DB/S3)


# Full Kafka workflow is:
* Run Docker to spin up Kafka + Zookeeper
* Create topic if needed
* Run producer script to post messages
* Run consumer script to receive them

## Post a Kafka Message Using Python
 ### Step 1: Install Kafka Python client
* pip install kafka-python
 ### Step 2: Python code to send a message
 ## kafka_producer.py
 from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

topic = 'test-topic'
message = 'Hello, Kafka!'

producer.send(topic, message.encode('utf-8'))
producer.flush()

print("Message sent!")


  
## Consume a kafka message
 ### Step 1: Install Kafka Python client
* pip install kafka-python

  ### Step 2: Consumer code to read messages
  ## kafka_consumer.py
  from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
)

print("Listening for messages...")

for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")

## Consume a kafka message to DB/S3  
## kafka_consumer.py
from kafka import KafkaConsumer
from write_to_db import write_to_db
from write_to_s3 import write_to_s3

consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='my-group'
)

for message in consumer:
    data = message.value.decode('utf-8')
    print(f"Received: {data}")

    # Write to DB or S3
    # Example: write_to_db(msg) or write_to_s3(msg)

    write_to_db(data) or
    write_to_s3(data)

  Also, write_to_db.py or write_to_s3.py needs to be present in the folder.
  ## write_to_db.py
  import sqlite3

def write_to_db(data):
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS messages (content TEXT)')
    c.execute('INSERT INTO messages (content) VALUES (?)', (data,))
    conn.commit()
    conn.close()

  ## write_to_s3.py
  import boto3
from datetime import datetime

bucket = "bucket_name"
aws_access_key_id = "accesskey"
aws_secret_access_key = "awssecretkey"
region_name = "region_name"

s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

def write_to_s3(data):
    key = f'messages/{datetime.now().isoformat()}.txt'
    s3.put_object(Bucket=bucket, Key=key, Body=data)
