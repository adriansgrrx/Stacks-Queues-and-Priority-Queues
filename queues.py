from collections import deque
from heapq import heappush
from heapq import heappop

# Building Queue(FIFO) data type
class Queue:
    # adding "*" to a parameter to have a varying number of positional argument and not just one
    def __init__(self, *elements): 
        self._elements = deque(elements)

    # using a built-in function __len__ to make function len() operational
    def __len__(self):
        return len(self._elements)

    # using a built-in function __iter__ to make the class iterable
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue() #yield is the same as return but it just pauses the execution of the function

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

# Building Stack(LIFO) data type
class Stack(Queue): # <-- Inheritance
    def dequeue(self):
        return self._elements.pop() # pop()  gets and removes the last element on the data.

# Representing Priority Queues With a Heap
# fruits = []

# heappush(fruits, "orange")
# heappush(fruits, "apple")
# heappush(fruits, "banana")
# print(fruits)

# # heappop gets the first element and the remaining element shuffles a little
# heappop(fruits)
# print(fruits)

person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

print(person1 < person2)
print(person2 < person3)