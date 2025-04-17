from kafka import KafkaConsumer


consumer = KafkaConsumer(
    'my-topic', #topic name should be as in producer
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='my-group'
)

for message in consumer:
    data = message.value.decode('utf-8')
    print(f"Received: {data}")

