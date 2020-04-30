## BeautifulSoup
### Installation:
```
sudo apt install python3-pip
pip3 install bs4
```
<br/>

```python
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html-parser')

# Retrieve all anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
```    
<br/>
When dealing with https we have to add these lines <br/>
```python
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url, context=ctx).read()
```
