# need to import
import re

# re.search
x = "My 2 favourite numbers are 19 and 42"
y = re.search("[0-9]+", x)
print(y)  # <re.Match object; span=(3, 4), match='2'>

# re. findall
y = re.findall("[0-9]+", x)
print(y)  # ['2', '19', '42']
# greedy matching means ^F.+: would match to "FRom: using the" instead of just "From:"
# can add ?  to make it not greedy ^F.+?:

# ex 1
userInput = input("Enter a regular expresion: ")
count = 0
fhand = open("files/mbox.txt")
for line in fhand:
    if re.search(userInput, line):
        count += 1
print(count)

# ex 2

fhand = open("files/mbox.txt")
list = []
for line in fhand:
    x = re.findall("^New Revision: [0-9]+", line)
    if len(x) > 0:
        y = int(re.findall("[0-9]+", x[0])[0])
        list.append(y)
print(sum(list)/len(list))
