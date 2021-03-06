# while loop
n = 5
while n > 0:
    print(n)
    n -= 1
print("done")

# break
while True:
    break
print("broken out")

# continue runs from start of loop
n = 0
while True:
    if n < 5:
        n += 1
        continue
    break
print(n)

# for loop
for i in [5, 4, 3, 2, 1]:
    print(i)
print("done")

# a for example
large = None
for i in [10, 56, 12, 4, 122, 1]:
    if large == None or i > large:
        large = i
print(large)

# "is" is deep equal
# 1.0 is not 1

# ex 1
# vars
count = 0
total = 0

# loop indefinitely
while True:
    # request user input
    userInput = input("Enter a number: ")
    # and cancel if done
    if userInput == "done":
        break

    # otherwise attempt to convert to float
    try:
        num = float(userInput)
    except:
        print("Invalid input")
        continue

    # if valid input then we can add to count and total
    count += 1
    total += num

# once done calculate average
if count > 0:
  avg = total / count
  print(total, count, avg)
else :
  print("No numbers entered")

#############

# ex 2
# vars
min = None
max = None

# loop indefinitely
while True:
    # request user input
    userInput = input("Enter a number: ")
    # and cancel if done
    if userInput == "done":
        break

    # otherwise attempt to convert to float
    try:
        num = float(userInput)
    except:
        print("Invalid input")
        continue

    # if valid input then we add to max min if required
    if min is None or num < min:
        min = num
    if max is None or num > max:
        max = num

# once done print
print(min, max)
