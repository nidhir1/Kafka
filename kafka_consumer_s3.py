from kafka import KafkaConsumer
from kafka_write_to_s3 import write_to_s3

consumer = KafkaConsumer(
    'my-topic', #topic name should be as in producer
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='my-group'
)

for message in consumer:
    data = message.value.decode('utf-8')
    print(f"Received: {data}")

    # Write to  S3

    write_to_s3(data)
