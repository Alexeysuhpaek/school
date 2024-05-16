from random import randint
from unicodedata import name

class Potion:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality
    def __str__(self):
        return f'Это зелье с именем: {self.name} и качеством {self.quality}'
 
 
    def __add__(self, other):
        new_quality= (self.quality+other.quality) //2
        new_name = self.name[:3]+other.name[3:]
        z = Potion(new_name,new_quality)
        z.check_quality()
        return z
    
    def check_quality(self):
        if self.quality> 50:
            print("хорошее зелье")
        else:
            print('зелье плохое')
g = Potion(name= "health",quality=randint(5,100))
s = Potion(name= "porcha",quality=randint(5,100))

print(g+s)