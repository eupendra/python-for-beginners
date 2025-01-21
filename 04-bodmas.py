# BODMAS (Brackets, Orders, Division/Multiplication, Addition/Subtraction)
# Implemented as PEMDAS (Brackets, Exponents, Division/Multiplication, Addition/Subtraction)
x = 5
x = x + 1
x += 1

print(x) # 7

r = 2 + 3 * 4 #14
print(r)

r = 2 + 3 * 4 ** 2 # 50
print(r)

r = 2 + 3 * 4 ** 2 / 1 + 1 # 51
print(r)

r = (2 + 3) * 4 ** 2 / (1 + 1) # 40
print(r)
