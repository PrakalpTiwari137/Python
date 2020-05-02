## Python Object
An Object is a bit of self-contained Code and Data. Objects have boundaries that allow us to ignore un-needed detail.<br/>
### Definitions:<br/>
1) Class : A template<br/>
2) Method or Message : A defined capability of a class<br/>
3) Field or attribute : A bit of data in a class<br/>
4) Object or Instance : A particular instance of a class<br/><br/>

### Object Lifecycle:<br/>
We have special blocks of code (methods) that get called at the moment of creation (constructor) and at the moment of destruction (destructor)<br/>

```python
class PartyAnimal:
    x = 0
    
    def __init__(self):
        print('I am constructed')
    
    def part(self):
        self.x = self.x + 1
        print('So far', self.x)
    
    def __del__(self):
        print('I am destructed')
        
an = PartyAnimal()  # I am constructed
an.party()          # So far 1
an.party()          # So far 2
an = 42             # I am destructed
```
**Note**: Constructors can have additional parmeters. These can be used to set up instance variables for the particular instance of the class (i.e. for the pparticular object).<br/>
```python
class PartyAnimal:
    name = ""
    def __init__(self,z):
        self.name = z
        printf(self.name,"constructed")

a = PartyAnimal("Sally")
```
<br/><br/>

### Object Inheritance
When wwe make a new class - we can reuse an existing class and **inherit** all the capabilities of an exisiting class and then add our own little bit to make our new class.<br/>
```python
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        ...
    
    def party(self):
        ...

#FootbalFan is a class which etends PartyAnimal. It has all capabilities that PartyAnimal has 
class FootballFan(PartyAnimal):     
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,"points",self.points)
        
s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
```
