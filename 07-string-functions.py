# Function: Independent, operates on input, globally accessible.
# Method: Associated with objects, operates on object data, called via object.

sentence = "Python for Technical Writers by Upendra"
# function
print()

# method
sentence.upper()

print(sentence.upper())

# original does not change
print(sentence)

print(sentence.find('T'))  # Also show `in` Operator

print(sentence.replace('Technical', 'All'))

# Strings are immutable
print(sentence)
