# EXERCISE
# Ask for the birth year
birth_year = int(input("Enter your birth year: "))
current_year = 2025  # Replace with the actual current year if necessary
age = current_year - birth_year
# print("You are " + age + " years old.")  # wont work

print("You are " + str(age) + " years old.")  # works
# BONUS TIP
print(f"You are {age} years old.")
####################
# SOLUTION TO BONUS
####################
# Ask for the user's name and birth year, then display the message
name = input("What's your name? ")
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print(f"Hey " + name + "! You are " + age + " years old.")
