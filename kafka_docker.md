# Kafka Docker 


## 📚 Table of Contents

1. [🧰 Prerequisites](#-prerequisites)
2. [🐳 Step 1: Setup Kafka with Docker](#-step-1-setup-kafka-with-docker)

---

## 🧰 Prerequisites

- Docker & Docker Compose
- Python 3.8+
- pip (Python package manager)
- Optional: PostgreSQL and AWS credentials for DB/S3

---

## 🐳 Step 1: Setup Kafka with Docker

1. Create a file named `docker-compose.yml`:

```yaml
version: '3.8'

services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000

  kafka:
    image: confluentinc/cp-kafka:latest
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1




#(Optional) Create topic manually: or else code.
docker exec -it your_kafka_container_name kafka-topics \
  --create --topic test-topic \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1

## Interact with Kafka
### Exec into the Kafka container:

* docker exec -it kafka bash

## Create a topic:
* kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

## List topics:

*kafka-topics --list --bootstrap-server localhost:9092
