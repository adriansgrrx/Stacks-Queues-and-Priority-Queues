from collections import deque

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

# ******************
# Testing Section
# ******************
# FIFO
# fifo = Queue()
# fifo.enqueue("1st")
# fifo.enqueue("2nd")
# fifo.enqueue("3rd")

# print(fifo.dequeue())
# print(fifo.dequeue())
# print(fifo.dequeue())

# fifo = Queue("1st", "2nd", "3rd")
# print(len(fifo))

# for element in fifo:
#     print(element)

# # this will return a vlaue of 0 after the iteration because of the built-in function __iter__
# print(len(fifo))

# LIFO
# lifo = Stack("1st", "2nd", "3rd")
# for element in lifo:
#     print(element) # This will return the descending order of the data, 
                    # wherein the Last entered element will pulled out until the first element.

# LIFO Data Type Alternative using list
lifo = []

lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

# This will return the same result
print(lifo.pop())
print(lifo.pop())
print(lifo.pop())