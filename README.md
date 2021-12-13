# Real Time Bus-tracker
Flask project which tracks the movement of Buses by consuming data produced by Kafka producer.

## Get Started

### Generate Bus Coordinates
Go to [Geo](https://geojson.io/#map=2/20.0/0.0) for generating bus-oordinates and store them in the `data` folder

### Kafka

---
**NOTE**

Start all of these steps in independent terminals.

---
1. Start Zookeeper
```
zookeeper-server-start.bat <path_to := zookeeper.properties> 
```
2. Start Kafka server
```
kafka-server-start.bat <path_to := server.properties> 
```
3. Creating Topic 
```
kafka-topics.bat --zookeeper localhost:2181 --topic geodata_final --create --partisions 1 --replication-factor 1 
```
4. Starting Topic Consumer
```
kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic geodata_final --from-beginning 
```
5. Starting Producer
```
python busdata1.py
python busdata2.py
```
### Flask App
1. Run server `flask run`
2. In browser open localhost:5001 and Voila you have successfully started bus-tracker

## Data  
1. The data folder contains the points for which we would like to visualize both the buses routes.
2. Production of data points at various interval is handled by Kafka's producers for a topic pre set/created by user.
