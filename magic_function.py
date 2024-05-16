# class Fuuu:
#     def __add__(self,number):
#         return Fuuu()
    
# a = Fuuu()
# b = Fuuu()
# print(a+b)







class Drobi:
    def __init__(self,chisl,znamen):
        self.chisl = chisl
        self.znamen = znamen
    def __str__(self):
        return f"{self.chisl}/{self.znamen}"
    def __add__(self,other):
        newchisl= self.chisl*other.znamen+other.chisl*self.znamen
        newznamen=self.znamen*other.znamen
        return Drobi(chisl=newchisl, znamen=newznamen)
    def __sub__(self,other):
        newchisl= self.chisl*other.znamen-other.chisl*self.znamen
        newznamen=self.znamen*other.znamen
        return Drobi(chisl=newchisl, znamen=newznamen)
d = Drobi(znamen= 8,chisl= 4)
s = Drobi(znamen= 2,chisl= 6)
print(s-d)
print(s+d)


d()
