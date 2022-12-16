from kafka import KafkaProducer

# The .send() method is asynchronous because it returns a future object that you can await by calling its blocking .get() method.
producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:
    message = input("Message: ")
    producer.send(
        topic="datascience",
        value=message.encode("utf-8"),
    )