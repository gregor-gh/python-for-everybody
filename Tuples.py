# tuples are like lists
x = ("Glen", "sally", "joe")
print(x[2])

# tuples are immutable
# x[2] = "nope"

# more efficient than lists

# can assign in multiples
(x, y) = (4, "Fred")
print(y)

# tuples are comperable
(0, 1, 2) < (5, 1, 2)  # true

# sort lists of tuples
d = {"a": 10, "b": 1, "c": 22}
print(d.items())
sorted(d.items())

for k, v in sorted(d.items()):
    print(k, v)

c = {"a": 10, "b": 1, "c": 22}
temp = []
for k, v in c.items():
    temp.append((v, k))

print(temp)

temp = sorted(temp, reverse=True)
print(temp)

fhand = open("files/romeo.txt")
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = []
for k, v in counts.items():
    newtup = (v, k)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for v, k in lst[:10]:
    print(k, v)

# list comprehension [] to craete generator for list elements
print(sorted([(v, k) for k, v in counts.items()]))

# ex 1
fhand = open("files/mbox.txt")
emailcount = {}

for line in fhand:
    words = line.split()
    try:
        first = words[0]
    except:
        continue
    if words[0] == "From":
        email = words[1]
        emailcount[email] = emailcount.get(email, 0) + 1
print(emailcount)

(k, v) = sorted([(v, k) for k, v in emailcount.items()], reverse=True)[0]
print(v, k)

# ex 2
fhand = open("files/mbox.txt")
timeCount = {}

for line in fhand:
    words = line.split()
    try:
        first = words[0]
    except:
        continue
    if words[0] == "From":
        time = words[5]
        hour = time.split(":")[0]
        timeCount[hour] = timeCount.get(hour, 0) + 1
print(timeCount)

hourlist = sorted(timeCount.items())
for entry in hourlist:
    (k, v) = entry
    print(k, v)

# ex 3
fhand = open("files/mbox.txt")
letterdict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
              "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

for line in fhand:
    for char in line:
        lowchar = char.lower()
        if lowchar in letterdict:
            letterdict[lowchar] += 1

print(letterdict)
letterList = sorted([(v, k) for k, v in letterdict.items()], reverse=True)
print(letterList)
