# strings are arrays of characters
fruit = "banana"
letter = fruit[1]
print(letter)  # a
letter = fruit[1 - 1]
print(letter)  # b

# strings are immutable, can't set fruit[1] to something else

# len for length
print(len(fruit))

# for through strings
for l in fruit:
    print(l)

# slicing
s = "Monty Python"
print(s[0:4])
# Mont
print(s[6:7])
# P
print(s[6:100])
# no traceback
print(s[:5])
# monty
print(s[8:])
# thon

# concat
a = "this " + "that"

# in as logical operatator
print("n" in "banana")  # true

# can sort and < > strings, but case is important

# string library, like prototype
print("THIS".lower())

# dir to print methods
print(type("THIS"))
print(dir("THIS"))

# find, if not found -1
fruit = "banana"
pos = fruit.find("na")
print(pos)  # 2

# replace
fruit = fruit.replace("n", "N")
print(fruit)

# trim aka strip
" test ".strip  # "test"
" test ".lstrip  # "test "
" test ".rstrip  # " test"

# startswith
"Test".startswith("T")  # true

# format operator
print("In %d years I have spotted %g %s" % (3, 0.1, "camels"))

# ord to get asci char code
print(ord("H")) # 72

# ex 1

test = "Sausages"
i = len(test)
while i > 0:
    print(test[i-1])
    i -= 1

# ex2 entire string

# ex3


def counter(word, let):
    count = 0
    for letter in word:
        if letter == let:
            count = count + 1
    return count


print(counter("banana", "a"))

# ex 4
print("banana".count("a"))

# ex 5
str = 'X-DSPAM-Confidence:0.8475'
colonIndex = str.find(":")
leftString = str[colonIndex + 1:]
trimString = leftString.strip()
print(float(trimString))
