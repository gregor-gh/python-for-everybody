# http sockets
from bs4 import BeautifulSoup
import urllib.error
import urllib.parse
import urllib.request
import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# attempst to call, will through error if no resposne from server
mysock.connect(("data.pr4e.org", 80))

# encode() into UTF-8
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

# loop through received data
while True:
    data = mysock.recv(512)  # receive data 512 characters at a time
    if (len(data) < 1):  # if there is no data left to receive break
        break
    # otherwise decode into Unicode unand print. end="" stops a new line being added after the 512 chars
    print(data.decode(), end="")

mysock.close()

######################

# use urlib instead, shorter, no headers by default

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt") # can use dict(fhand.getheaders()) 
for line in fhand:
    print(line.decode().strip())

fhand = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
for line in fhand:
    print(line.decode().strip())

###########################

# beautiful soup to scrape page

url = "http://www.dr-chuck.com/page1.htm"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# retrieve all anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))

####################

# dowonload an image
HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if (len(data) < 1):
        break
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("files/stuff.jpg", "wb")
fhand.write(picture)
fhand.close()

######################

# ex 1 and 2

userinput = input("Enter url")
start = re.findall("^http:\/\/[\w|\.]+", userinput)
if len(start) > 0:
    inputArray = start[0].split("//")
    if len(inputArray) > 1:
        domain = inputArray[1]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# attempst to call, will through error if no resposne from server
mysock.connect((domain, 80))

# encode() into UTF-8
req = "GET " + userinput+" HTTP/1.0\r\n\r\n"
cmd = req.encode()
mysock.send(cmd)

text = ""

# loop through received data
while True:
    data = mysock.recv(512)  # receive data 512 characters at a time
    if (len(data) < 1):  # if there is no data left to receive break
        break
    # otherwise decode into Unicode unand store. end="" stops a new line being added after the 512 chars
    text+=(data.decode())

mysock.close()

## print first 3000 chars only
print(text[:3000], len(text))

# ex 3

text=""

fhand = urllib.request.urlopen("http://data.pr4e.org/mbox.txt")
for line in fhand:
    text+=line.decode().strip()

## print first 3000 chars only
print(text[:3000], len(text))

# ex 4

url = "https://books.trinket.io/pfe/12-network.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# retrieve all anchor tags
tags = soup("p")
print(len(tags))