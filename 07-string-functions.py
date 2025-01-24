# Function: Independent, operates on input, globally accessible.
# Method: Associated with objects, operates on object data, called via object.

sentence = "Python for Technical Writers by Upendra"
# function
print()

# method (limited to an object)
sentence.upper()

print(sentence.upper())

# original does not change, Strings are immutable
print(sentence)

print(sentence.index('P'))  # Also show `in` Operator


print(sentence.replace('Technical Writers', 'Everyone'))


# Strings are immutable
print(sentence)
