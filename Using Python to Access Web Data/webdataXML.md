## Data formats
### XML (eXtensible Markup Language)
**Terminology**:<br/>
***1) Tags***  indicate the beginning and ending of elements.<br/>
***2) Attributes***  are keyword/value pairs on the opening tag of XML.<br/>
***3) Serialize/de-serialize***  convert data in one program into a common format that can be stored and/or transmitted between systems in a programming language-independent manner.<br/><br/>

**XML as a tree**
```xml
<a>
    <b w="5">X</b>
    <c>
        <d>Y</d>
        <e>Z</e>
    <c>
</a>
```
currNode: a ;   childNode1: b   ; childNode2: c ;<br/>
currNode: b ;   childNode1: 5   ; childNode2: X         ; <br/>
currNode: c ;   childNode1: d   ; childNode2: e ;<br/>
currNode: d ;   childNode1: Y         ; <br/>
currNode: e ;   childNode1: Z         ; <br/><br/>

**XML Schema**: Describing a contract as to what is acceptable XML.<br/>

Example code:<br/>
```python
import xml.etree.ElementTree as ET
data = '''
        <person>
            <name>Chuck</name>
            <phone type = "intl">
                +1 734 303 4456
            </phone>
            <email hide = "yes"/>
        </person>
        '''
tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
```

<br/>**Case**: When we have multiple childs
```python
import xml.etree.ElementTree as ET
input = '''
        <stuff>
            <users>
                <user x="2">
                    <id>001</id>
                    <name>Chuck</name>
                </user>
                <user x="7">
                    <id>009</id>
                    <name>Brent</name>
                </user>
            </users>
        </stuff>
        '''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')   #List of tags (not strings)
print('User count:',len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id',item.find('id').text)
    print('Attribute', item.get("x"))
```
