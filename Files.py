# file handles
fhand = open("files/test.txt")
print(fhand)

# \n is newline

# use for to read lines in file
# for line in fhand:
#    print(line)

# or use read to read in one go
#inp = fhand.read()
# print(inp)

# use rsytrip to trim extra newline
for line in fhand:
    line = line.rstrip()
    print(line)

# can use inpuit to set filename

# use continue to use cnditional logic

# try except for bad filenames

# ex 1

fhand = open("files/mbox-short.txt")
for line in fhand:
  print(line.upper())

# ex 2 and 3
userInput = input("Enter filename: ")
if userInput == "na na boo boo":
  print("easter egg")
else:
  fhand = open("files/" + userInput + ".txt")

  count = 0
  total = 0

  for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
      colonIndex = line.find(":")
      leftString = line[colonIndex + 1:]
      trimString = leftString.strip()
      total += float(trimString)
      count+=1

  avg=total/count
  print("Average spam confidence:", avg)


