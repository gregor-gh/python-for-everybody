# def for functions
import math
import random


def thing():
    print("hello")


thing()
thing()

# max and min work on strings
big = max("hello world")
print(big)

# rand between 0 and 9.99999999
print(random.random())
print(random.randint(5, 10))
t = [1, 2, 3, 4, 5]
print(random.choice(t))

# math has lotsof functions
print(math.sin(0.7))
print(math.sqrt(4))


# args
def greet(lang):
    if lang == "es":
        print("Hola")
    else:
        print("Hello")


greet("es")
greet("en")

# return values


def square(n):
    return n ** 2


print(square(3))

# ex 6


def calcPay(hours, rate):

    # calc pay
    pay = hours * rate

    # multiply hours above 40 by 0.5
    if hours > 40:
        pay += (hours - 40) * rate * 0.5

    return pay


strhours = input("Enter Hours: ")
try:
    hours = float(strhours)
except:
    print("Invalid hours applied default of 40")
    hours = 40.0

# get rate and convert to float
strrate = input("Enter Rate: ")
try:
    rate = float(strrate)
except:
    print("Invalid rate, applied default of 10")
    rate = 10

# print final calc
print(calcPay(hours, rate))

# ex 7


def calcScore(score):
    if score <= 1.0:
        if score >= 0.0:
            if score >= 0.9:
                return "A"
            elif score >= 0.8:
                return "B"
            elif score >= 0.7:
                return "C"
            elif score >= 0.6:
                return "D"
            else:
                return "F"
        else:
            return "Bad score"
    else:
        return "Bad score"


score = input("Enter score: ")

try:
    score = float(score)
except:
    score = -1.0

print(calcScore(score))
