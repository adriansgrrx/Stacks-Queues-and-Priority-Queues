from queues import Queue

# fifo = Queue()
# fifo.enqueue("1st")
# fifo.enqueue("2nd")
# fifo.enqueue("3rd")

# print(fifo.dequeue())
# print(fifo.dequeue())
# print(fifo.dequeue())

fifo = Queue("Kylee Arroyo", "Randall Forbes", "Matthew Frazier", "Nyasia Hubbard", "Damaris Hooper")
print(f"\nElement size before: {len(fifo)}\n")

item = 1
for element in fifo:
    print(f"{item}) {element}")
    item += 1

# this will return a value of 0 after the iteration because of the built-in function __iter__
print(f"\nElement size after: {len(fifo)}\n")