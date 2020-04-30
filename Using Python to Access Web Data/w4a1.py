import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup

# url = 'http://py4e-data.dr-chuck.net/comments_481549.html'

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

val = 0

# find all elements having span tag 
lst = soup.find_all('span')
for line in lst:
    val = val + int(line.get_text())    # get the contents of the tag
print(val)
