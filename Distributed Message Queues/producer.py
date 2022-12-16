# Integrating Python With Distributed Message Queues
import pika

QUEUE_NAME = "mailbox"

# You can keep publishing messages read from the user.
with pika.BlockingConnection() as connection:
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    while True:
        message = input("Message: ")
        channel.basic_publish(
            exchange="",
            routing_key=QUEUE_NAME,
            body=message.encode("utf-8")
        )