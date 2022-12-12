from queues import Stack

# LIFO Data Type Alternative using list
# lifo = []

# lifo.append("1st")
# lifo.append("2nd")
# lifo.append("3rd")

# # This will return the same result
# print(lifo.pop())
# print(lifo.pop())
# print(lifo.pop())

lifo = Stack("Kylee Arroyo", "Randall Forbes", "Matthew Frazier", "Nyasia Hubbard", "Damaris Hooper")

item = 1
for element in lifo:                # This will return the descending order of the data, 
    print(f"{item}) {element}")    # wherein the Last entered element will pulled out until the first element.
    item += 1               
    