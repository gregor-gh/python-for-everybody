# print to console
print("hello")

# can also seperate with commas, will add spaces
print("hello", "world")

# set var
x = 1
print(x)

# addition
x = x + 5
print(x)

# subtraction
x = x - 1
print(x)

# multiplication
x = x * 2
print(x)

# division, forces result to float in py3 (not in py2)
x = x / 5
print(x)

# floor division
# 5 // 2 = 2

# power
x = x ** 3
print(x)

# modulus
x = x % 3
print(x)

# get type
t = type(x)
print(t)

# type conversion
t2 = int(x)
print(t2)
print(type(t2))

# can't add string and int
# z = "123"+4 Exception has occurred: TypeError

# convert to int to add
z = int("123") + 4
print(z)

# await input
#name = input("Enter name: ")
#print("Hello", name)

# exercises

# 2
name = input("Enter your name: ")
print("Hello", name)

# 3
hours = input("Enter hours: ")
rate = input("Enter Rate: ")
pay = round(float(rate) * float(hours), 2)
print("Pay:", pay)

# 4
width = 7
height = 12.0
print(width // 2)
print(width / 2.0)
print(height / 3)
print(1 + 2 * 5)

# 5
cel = float(input("Enter temp in C: "))
far = round(cel * 9 / 5 + 32, 1)
print(far)
