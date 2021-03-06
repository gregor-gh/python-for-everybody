# basically js objectrs
purse = dict()  # {} works too
purse["money"] = 12
purse["candy"] = 3
purse["tissues"] = 75
print(purse)

print(purse["candy"])

jjj = {
    "chuck": 1,
    "fred": 42,
    "jan": 100,
}
print(jjj)

# can't reference keys which do not exist
# jjj["bob"] errors

# can use in to get around this
counts = {"bob": 2}
names = ["bob", "darren", "Gavin"]

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

# or use get
counts = {"bob": 2}
names = ["bob", "darren", "Gavin"]

for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# list to convert to array
print(list(jjj))

# get keys
print(jjj.keys())

# get values
print(jjj.values())

# get items
print(jjj.items())

# two iteration values
for a, b in jjj.items():
    print(a, b)

# ex 1

fhand = open("files/mbox-short.txt")
dictionary = {}
for line in fhand:
    words = line.split()
    for word in words:
        dictionary[word] = 0

if "sausages" in dictionary:
    print("yes")
else:
    print("no")

# ex 2
fhand = open("files/mbox.txt")
wordcount = {}

for line in fhand:
    words = line.split()
    try:
        first = words[0]
    except:
        continue
    if words[0] == "From":
        day = words[2]
        wordcount[day] = wordcount.get(day, 0) + 1
print(wordcount)

# ex 3
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

# ex 4
print(max(emailcount), emailcount[max(emailcount)])

# ex 5
fhand = open("files/mbox.txt")
domaincount = {}

for line in fhand:
    words = line.split()
    try:
        first = words[0]
    except:
        continue
    if words[0] == "From":
        domain = words[1].split("@")[1]
        domaincount[domain] = domaincount.get(domain, 0) + 1
print(domaincount)
