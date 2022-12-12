from queues import Stack
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

lifo = Stack("1st", "2nd", "3rd")
for element in lifo:
    print(element) # This will return the descending order of the data, 
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