# What is Kafka?
Apache Kafka is a distributed event streaming platform. Think of it like a messaging system that lets different parts of your application (or different applications altogether) talk to each other by sending messages (called events) through topics.

* Producer: Sends data (events) to Kafka topics.

* Consumer: Reads data from Kafka topics.

* Broker: A Kafka server that stores and serves the data.

* Topic: A category or feed name to which messages are published.

# Kafka Architecture

##Text Description of Kafka Architecture (Simple Flow)

[Producers] ---> [Kafka Broker / Cluster] ---> [Consumers]
                       |
                 [Topics (Partitions)]
                       |
                 [Zookeeper / Kafka Controller]
                 
### Components:
##### Producers: Applications or services that send (publish) data to Kafka.

#### Kafka Broker: Core Kafka server that receives, stores, and forwards data.

#### Topics: Categories where records are published. Each topic can have multiple partitions for parallelism.

#### Consumers: Applications or services that read (subscribe to) data from Kafka topics.

#### Zookeeper / Kafka Controller: Manages Kafka brokers (leader election, configs, etc.).

##Kafka Architecture Flowchart
![image](https://github.com/user-attachments/assets/554bb1b5-2a8d-4d6d-9491-d1e1b9b09a06)

A Topic is not a separate entity from a Broker.

It is a logical concept that lives inside Kafka Brokers.

Physically, a Topic is stored as partitions across one or more Brokers.

What happens technically:
When you create a topic, Kafka assigns its partitions across multiple Brokers.

Each partition is a commit log stored on disk by a Broker.

One Broker will be the leader for a given partition, and others may be followers for replication.

Example:
You have 3 Brokers: B1, B2, B3.

You create a Topic "orders" with 3 partitions.

Partition 0 could be on B1, Partition 1 on B2, Partition 2 on B3.

So, topics are stored and managed by Brokers, and the actual data is split across partitions that physically live on the Brokers' storage.

![image](https://github.com/user-attachments/assets/a25eb0d5-858e-4178-b564-eeb570aebf63)


![image](https://github.com/user-attachments/assets/d85ae14f-3ffa-480c-9271-4ee1d2d120d5)

# What is a Data Pipeline?
* A data pipeline is a series of steps where data is collected, processed, and moved from one system to another. For example:

* Collect logs from a web server.

* Stream/process those logs to clean/transform the data.

* Store the final data into a database or data lake.

🧩 How Kafka Fits Into a Pipeline:
Kafka often acts as the backbone of modern data pipelines. Here’s a typical flow:


[App / Device / Service] 
      ↓
  Kafka Producer → [Kafka Topic] → Kafka Consumer → [Processing Engine / DB / Data Lake]
  
Example Use Case:
Let’s say you have a POS system and you want to build a real-time dashboard:

Each sale is published to a Kafka topic (producer).

A Kafka consumer reads the events.

The events are processed (e.g., add tax, analyze trends).

Final results are stored in a database or pushed to a dashboard.

