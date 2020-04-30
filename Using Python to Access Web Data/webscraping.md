## BeautifulSoup
### Installation:
```
sudo apt install python3-pip
pip3 install bs4
```

### Sample code:

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
### Tutorial:
When we perform web scraping, we're interested in the main content of the web page i.e. HTML<br/>
The most basic tag is `<html>` tag.<br/>
Right inside an `html` tag, we put two other tags, the `head` tag, and the `body` tag. Main content goes into `body` tag. <br/>
`p` tag defines a paragraph.<br/>
`a` tag are links, and tell the browser to render a link to another web page. The `href` property of the tag determines where the link goes.<br/><br/>

`a`, `p`, `div`, `b`, `i`, `table`, `form` are common html tags.<br/><br/>
`class` and `id` properties: One element can have multiple classes, and a class can be shared between elements. Each element can only have one id, and an id can only be used once on a page.<br/>

#### Parsing a page with BeautifulSoup

