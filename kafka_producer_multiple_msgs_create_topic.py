from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
import json
import time

TOPIC_NAME = 'test-topic1'

# Create topic if it doesn't exist
def create_topic(topic_name):
    try:
        admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092')
        topic_list = [NewTopic(name=topic_name, num_partitions=1, replication_factor=1)]
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print(f"Topic '{topic_name}' created.")
    except Exception as e:
        print(f"Topic '{topic_name}' may already exist or error occurred: {e}")

create_topic(TOPIC_NAME)

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
