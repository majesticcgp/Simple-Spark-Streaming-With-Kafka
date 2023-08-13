
# READ ME

This project using package version below
* Spark: 3.3.2
* Scala: 2.13.8
* Java: 8
* Python: 3.9.12 (This package was included in Anaconda)
* Kafka: 3.5.1
* Anaconda: 4.12.0

## How Install Kafka and Spark for Linux

* Kafka: https://www.linuxtechi.com/how-to-install-apache-kafka-on-ubuntu/
* Spark: https://linuxhint.com/install-pyspark-ubuntu-22-04/
* Anaconda: https://www.hostinger.com/tutorials/how-to-install-anaconda-on-ubuntu/

## Here is step by step to run project
You must cd to your kafka directory
* Step 1: START ZOOKEEPER 
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```
<img width="400" alt="image" src="https://github.com/nhatphongcgp/Simple-Spark-Kafka/assets/60643737/850501ce-f8d8-43a8-afec-d4e6e53f1878">

* Step 2: START BROKER 
```bash
bin/kafka-server-start.sh config/server.properties
```
<img width="400" alt="image" src="https://github.com/nhatphongcgp/Simple-Spark-Kafka/assets/60643737/7a6d852c-84e4-43fd-ace4-f99a36593482">

* Step 3: Create 2 topics (One for producer and the last one for consumer message from spark with writesteam)
```bash
bin/kafka-topics.sh \
--bootstrap-server localhost:9092 \
--create \
--replication-factor 1 \
--partitions 1 \
--topic json-data-topic
```

```
bin/kafka-topics.sh \
--bootstrap-server localhost:9092 \
--create \
--replication-factor 1 \
--partitions 1 \
--topic read-json-data-topic
```
<img width="591" alt="image" src="https://github.com/nhatphongcgp/Simple-Spark-Kafka/assets/60643737/37addb7b-f4cd-4cad-9a70-bd575b2c7179">

Step 4: RUN FILE main.py
 - In this step I open project with VSCODE
 - You must cd to project containt this file main.py
 - Because we integrate kafka with PySpark so we must add this option: --packages org.apache.spark:spark-sql-kafka-0-10_2.13:3.3.2
 - This option base on current version spark and scala we use in this project

```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.13:3.3.2 main.py
```
<img width="500" alt="image" src="https://github.com/nhatphongcgp/Simple-Spark-Kafka/assets/60643737/d4fff00e-8269-48b1-92d5-fffe742304b2">

Step 5: START CONSOLE PRODUCER
 * Start producer
```bash
bin/kafka-console-producer.sh \
--broker-list localhost:9092 \
--topic json-data-topic
```
 * Add message to producer
<img width="600" alt="image" src="https://github.com/nhatphongcgp/Simple-Spark-Kafka/assets/60643737/fd2925fe-49b6-47f9-a536-2f4ec11ba928">

 Step 6: BACK TO VSCODE
 * We get result
<img width="638" alt="image" src="https://github.com/nhatphongcgp/Simple-Spark-Kafka/assets/60643737/e996fe89-22f8-4a61-aa9e-4151972510aa">

 Step 7: START CONSOLE CONSUMER (If you want to learn write to console with spark streaming)
 ```bash
bin/kafka-console-consumer.sh \
--bootstrap-server localhost:9092 \
--topic read-json-data-topic
```
<img width="781" alt="image" src="https://github.com/nhatphongcgp/Simple-Spark-Kafka/assets/60643737/c2f5ce7e-3170-4602-95a3-6baba741476c">

Step 8: CHANGE SOMES LINES IN main.py
  * Make a checkpoint dir on your machine
  * Add some message in producer
<img width="1013" alt="image" src="https://github.com/nhatphongcgp/Simple-Spark-Kafka/assets/60643737/179770fc-6b1d-4f44-91f3-bbc6dabbfda4">
  * Back to console consumer to read new messages
<img width="1038" alt="image" src="https://github.com/nhatphongcgp/Simple-Spark-Kafka/assets/60643737/1161b994-bafc-4d67-8432-5906382cb3f7">




 
