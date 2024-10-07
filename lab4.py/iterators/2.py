b = int(input())
class dou:
    def __init__(self,b):
        self.b = b
        self.a = 0
    
    def __iter__(self):
        return self 
    def __next__(self):
        x=self.a
        if self.a <= self.b:
            self.a+=2
            return x
        else:
            raise StopIteration 
d = dou(b)
myiter = iter(d)
for x in myiter:
    print(x)
