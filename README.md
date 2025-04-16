# Kafka

# 🧵 Kafka - Message Queue Concepts

## 📚 Table of Contents

1. [What is a Message Queue?](#1-what-is-a-message-queue)
2. [Use Cases of Message Queues](#2-use-cases-of-message-queues)
3. [Database vs Message Queue – Differences and When to Use What](#3-database-vs-message-queue--differences-and-when-to-use-what)
4. [Advantages and Disadvantages of Message Queues](#4-advantages-and-disadvantages-of-message-queues)
5. [Why Message Queues are Used?](#5-why-message-queues-are-used)

---

## 1. What is a Message Queue?

A **Message Queue (MQ)** enables asynchronous communication between parts of a system. One component (producer) sends a message, and another component (consumer) processes it later.

**How it works:**
- **Producer** → sends a message
- **Queue** → stores it temporarily
- **Consumer** → retrieves and processes it

**Examples**: RabbitMQ, **Kafka**, AWS SQS, ActiveMQ

### 💡 Kafka-specific Note:
Kafka is not a traditional MQ — it's a **distributed log** that supports **persistent storage**, **replay**, and **high throughput**.

---

## 2. Use Cases of Message Queues

Typical MQ use cases:
- 🛒 Order processing
- 📩 Email/SMS notification systems
- 📹 Video/audio processing
- 🧩 Microservice communication
- 🔁 Retry/failure handling

### Kafka-Specific Use Cases:
- 🔄 Event sourcing & audit logs
- 📊 Real-time analytics
- 📈 Stream processing
- 📥 Ingesting IoT or telemetry data
- 🔄 Change Data Capture (CDC)

---

## 3. Database vs Message Queue – Differences and When to Use What

| Feature               | Database                            | Message Queue (MQ)                     |
|----------------------|-------------------------------------|----------------------------------------|
| **Purpose**          | Persistent, structured storage      | Temporary/persistent communication     |
| **Communication**    | Synchronous                         | Asynchronous                           |
| **Ordering**         | Based on index/schema               | Maintained (per partition in Kafka)    |
| **Scalability**      | Harder to scale                     | Highly scalable                        |
| **Retry Mechanism**  | Manual handling                     | Built-in in most MQs                   |
| **Use Case Fit**     | CRUD apps, reporting                | Decoupling, async tasks, streaming     |

### Use a Database When:
- You need durable, queryable data
- You need ACID transactions

### Use Kafka When:
- You want asynchronous, scalable
