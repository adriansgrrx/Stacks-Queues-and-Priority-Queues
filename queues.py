from collections import deque
from heapq import heappush, heappop
from itertools import count

# Refactoring the Code Using a Mixin Class
class IterableMixin:                    # Made a new class that will provide len() and the same time
    def __len__(self):                  # an iteration. Then, inherited in Queue and PriorityQueue class.
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

# Building Queue(FIFO) data type
class Queue(IterableMixin):
    # adding "*" to a parameter to have a varying number of positional argument and not just one
    def __init__(self, *elements): 
        self._elements = deque(elements)

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

# Building Stack(LIFO) data type
class Stack(Queue): # <-- Inheritance
    def dequeue(self):
        return self._elements.pop() # pop() gets and removes the last element on the data.

# Building a Priority Queue Data Type
class PriorityQueue(IterableMixin):
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value) # the _counter will be responsible for handling 
                                                            # the same priority description making the 
                                                            # first enqueued be the first by default.  
        heappush(self._elements, element) # rearranging heappush parameters
    def dequeue(self):
        return heappop(self._elements)[-1] # to indicate the last component of the tuple, 
                                            #regardless of its length, -1 was implemented as the index 
                                            # of the tuple