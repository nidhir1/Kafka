from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
import json
import time

TOPIC_NAME = 'test-topic1'


# Initialize Kafka producer with JSON serializer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Sample messages to send
messages = [
    {"user": "alice", "action": "login"},
    {"user": "bob", "action": "upload", "file": "report.pdf"},
    {"user": "carol", "action": "logout"}
]

for msg in messages:
    try:
        print(f"Sending message: {msg}")
        producer.send(TOPIC_NAME, msg)
        time.sleep(1)  # simulate delay
    except Exception as e:
        print(f"Error sending message: {e}")

producer.flush()
print("All messages sent!")
