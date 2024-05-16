class Foo:
    def __init__(self,color, size_memory):
        # print(self,"это внутри иннита")
        self.color=color
        self.size_memory=size_memory
        self.company="Sony"
        self.fact_memory=self.size_memory -27
    
    def on(self):
        print ("neneyneley приставка включена")

ps5 = Foo("white", 512)
print(ps5.color)
ps5.color="purple"
print(ps5.color)
ps5.status="crash"
ps6 = Foo("red",1002)
print(ps6)
ps5.on()