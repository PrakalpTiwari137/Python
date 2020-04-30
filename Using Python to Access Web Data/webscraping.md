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
soup = BeautifulSoup(html, 'html.parser')

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
**Step1**: Download the website
```python
import urllib.request, urllib.parse, urllib.error

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
```
<br/> **Step2**: Create an instance of `BeautifulSoup` class to parse our document:
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
```
We can print the HTML content, formatted nicely, using `prettify` method
```python
print(soup.prettify())
```
Once we've isolated a tag, we can use the `get_text()` method to extract all of the text inside the tag.<br/><br/>

#### Finding all instances of a tag at once
`find_all` method finds all instances of a tag on a page.
```python
soup = BeautifulSoup(html, 'html.parser')
soup.find_all('p')
```
**Note**: `find_all` returns a list. We have to loop through, or use list indexing to extract text:
```python
soup.find_all('p')[0].get_text()
```
<br/><br/>

#### Searching for tags by class and id
We can use `find_all` method to search for elements by class or by id.
<br/>1) `p` tag that has class `outer-text`:
```python
soup.find_all('p', class_='outer-text')
```
<br/>2) Any tag that has the class `outer-text`:
```python
soup.find_all(class_='outer-text')
```
<br/>3) Search for elements by id:
```python
soup.find_all(id='first')
```
<br/><br/>

#### Using CSS Selectors
Examples of CSS selectors:<br/>
1) `p a` - finds all `a` tags inside of a `p` tag<br/>
2) `body p a` - finds all `a` tags inside of a `p` tag inside of a `body` tag.<br/>
3) `p.outer-text` - finds all `p` tags with a class of *outer-text*.<br/>
4) `p#first` - finds all `p` tags with an id of *first*<br/><br/>
`BeautifulSoup` objects support searching a page via CSS selectors using the `select` method.
```python
soup.select('div p')
```
`select` method returns a list of `BeautifulSoup` objects, just like `find_all`.



