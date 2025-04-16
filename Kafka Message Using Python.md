1. [ Post a Message using Python](#post-a-Kafka-message-using-python)
2. [ Consume and Write to DB/S3](#consume-a-kafka-message-and-write-to-db/S3)
3. [ Notes & Troubleshooting](#-notes--troubleshooting)

# Full Kafka workflow is:
* Run Docker to spin up Kafka + Zookeeper
* Create topic if needed
* Run producer script to post messages
* Run consumer script to receive them

## Post a Kafka Message Using Python
 ### Step 1: Install Kafka Python client
* pip install kafka-python
 ### Step 2: Python code to send a message
 from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

topic = 'test-topic'
message = 'Hello, Kafka!'

producer.send(topic, message.encode('utf-8'))
producer.flush()

print("Message sent!")


  
## Consume a kafka message and write to db/S3


  
