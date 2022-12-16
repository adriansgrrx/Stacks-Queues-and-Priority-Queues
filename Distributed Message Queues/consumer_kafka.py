from kafka import KafkaConsumer

# the consumer receives the message and will display it out using iteration.
consumer = KafkaConsumer("datascience")
for record in consumer:
    message = record.value.decode("utf-8")
    print(f"Got message: {message}")