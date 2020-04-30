## HTTP request in Python
```python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while(True):
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()
```

<br/>This action is so common that there is a library for it: `urllib`
```python
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
```

<br/>Note: The output of this will only contain text in the file. Headers are omitted.<br/>
Using this method we can treat the document as a file!!!<br/>
This can be used not only to read text files but also html pages.


