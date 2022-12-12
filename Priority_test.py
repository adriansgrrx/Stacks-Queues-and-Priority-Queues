from queues import PriorityQueue
# ***********************INTRODUCTION FOR PRIORITY QUEUE********************************
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
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

print(messages.dequeue()) #Critical
print(messages.dequeue()) #Important, Windshield wipers turned on
print(messages.dequeue()) #Important, Hazard lights turned on
print(messages.dequeue()) #Neutral