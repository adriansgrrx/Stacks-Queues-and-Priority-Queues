import redis

# Redis server instance will immediately start publishing messages on the chatroom channel.
with redis.Redis() as client:
    while True:
        message = input("Message: ")
        client.publish("chatroom", message)