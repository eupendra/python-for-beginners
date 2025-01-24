# List
fruits = ["apple", "banana", "cherry", "dates"]
print(type(fruits))
print(fruits)


for f in fruits:
    print(f)

print(fruits[0])
print(fruits[-1])

fruits[0] = "avocado"

print(fruits[1:2])

print(fruits[1])  # Indexing
print(fruits[1:])  # Slicing

# Syntax
# list[start:stop:step]


fruits.append("Elderberry")
fruits.insert(2, "berry")
fruits.insert(2, 100)  # list can have mixed types

print(fruits)

#
#
# # Tuple
# coordinates = (10.0, 20.0)
# print(type(coordinates))  # Output: <class 'tuple'>
#
# # Dictionary
# person = {
#     "name": "Upendra",
#     "age": 100
# }
# print(type(person))  # Output: <class 'dict'>
#
# # NoneType
# unknown = None
# print(type(unknown))  # Output: <class 'NoneType'>
