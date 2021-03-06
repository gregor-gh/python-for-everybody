# comparison == != < <= > >= is is not


# if else. colon followed by indent. can do same line instead. elif is elseif. can chain
x = 4
if x > 2:
    print("bigger")
elif x == 2:
    print("Same")
else:
    print("smaller")
print("done")

# try except is try catch
exampleinput = "hello"
try:
  convinput = int(exampleinput)
except:
  print("error")

# 1
# get hours and convert to float
strhours = input("Enter Hours: ")
try :
  hours = float(strhours)
except :
  print("Invalid hours applied default of 40")
  hours = 40.0

# get rate and convert to float
strrate = input("Enter Rate: ")
try :
  rate = float(strrate)
except:
  print("Invalid rate, applied default of 10")
  rate = 10

# calc pay
pay = hours * rate

# multiply hours above 40 by 0.5
if hours > 40:
  pay+=(hours-40)*rate*0.5

# print final calc
print(pay)

#########

# 2 already done essentially

# 3 

score = input("Enter score: ")

try:
  score = float(score)
except:
  score= -1.0

if score <= 1.0:
  if score >= 0.0:
    if score >= 0.9:
      print("A")
    elif score >= 0.8:
      print("B")
    elif score >= 0.7:
      print("C")
    elif score >= 0.6:
      print("D")
    else:
      print("F")
  else:
    print("Bad score")
else:
  print("Bad score")




