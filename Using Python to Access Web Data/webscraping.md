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

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
```    
k
