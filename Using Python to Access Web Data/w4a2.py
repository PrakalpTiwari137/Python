import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup

#url = 'http://py4e-data.dr-chuck.net/known_by_Kirsty.html'
#count = 4
#position = 3
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

# find all elements having span tag 
lst = soup.find_all('a')
line = lst[position-1]
name = None
print('Retrieving:',url)

while count:
    url = line.get('href',None)
    print('Retrieving:',url)
    name = line.get_text()
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    lst = soup.find_all('a')
    line = lst[position-1]
    count = count-1
print(name)
