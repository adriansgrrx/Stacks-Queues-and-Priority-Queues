from queues import Stack

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