from queues import PriorityQueue
# ***********************INTRODUCTION FOR PRIORITY QUEUE*******************************
# # Representing Priority Queues With a Heap
# fruits = []

# heappush(fruits, "orange")
# heappush(fruits, "apple")
# heappush(fruits, "banana")
# print(fruits)

# # heappop gets the first element and the remaining element shuffles a little
# heappop(fruits)
# print(fruits)

# person1 = ("John", "Brown", 42)
# person2 = ("John", "Doe", 42)
# person3 = ("John", "Doe", 24)

# print(person1 < person2)
# print(person2 < person3)

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Eat breakfast")
messages.enqueue_with_priority(NEUTRAL, "Wear perfume")
messages.enqueue_with_priority(NEUTRAL, "Put a jacket on")
messages.enqueue_with_priority(CRITICAL, "Wake up early")
messages.enqueue_with_priority(IMPORTANT, "Take a shower")

print(messages.dequeue()) #Critical
print(messages.dequeue()) #Important, Eat breakfast
print(messages.dequeue()) #Important, Take a shower
print(messages.dequeue()) #Neutral, Wear perfume
print(messages.dequeue()) #Neutral, Put a jacket on

