# list is basically array
x = [1, 2, [4, 5]]

# range creates a list
y = range(4)
for i in y:
    print(i)

# can use to create an indexed for
friends = ["Bob", "Glenn", "Gav"]
for i in range(len(friends)):
    print(i, friends[i])

# can concat lists with +
print([1, 2, 3] + [4, 5, 6])

# can slice list
print([1, 2, 3, 4, 5, 6][1:3])

# can create empty list using [] or list()
l = list()

# can add to end with append
l.append("test")
l.append(99)
print(l)

# can use in to check if something is in a list

# can sort with sort(). sorts list in place
friends = ["Bob", "Glenn", "Gav"]
friends.sort()
print(friends)

# can use sum() min() max() len()

# split can pass in text to split by as first arg
abc = "with three words"
stuff = abc.split()
print(stuff)

# ex 1


def chop(list):
    list = list[1:len(list)-1]
    print(list)
    return None


chop([1, 2, 3, 4, 5])


def middle(list):
    return list[1:len(list)-1]


print(middle([1, 2, 3, 4, 5]))

# ex 2 and 3

fhand = open('files/test.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) != 0 and words[0] == "From":
        try:
            print(words[2])
        except:
            continue

# ex 4
fhand = open("files/romeo.txt")
wordList = []

for line in fhand:
    words = line.split()
    for word in words:
        if word not in wordList:
            wordList.append(word)
wordList.sort()
print(wordList)

# ex 5
fhand = open("files/mbox-short.txt")

count = 0

for line in fhand:
    if line.startswith("From") and line[4] != ":":
        words = line.split()
        count += 1
        print(words[1])
print(count)

# ex 6

# vars
arr = []

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
    arr.append(num)

# once done print
print(max(arr))
