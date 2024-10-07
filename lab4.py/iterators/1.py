b = int(input())
class dou:
    def __init__(self,b):
        self.b = b
        self.a = 1
    
    def __iter__(self):
        return self 
    def __next__(self):
        x=self.a
        if self.a <= self.b:
            res = x*x
            self.a+=1
            return res
        else:
            raise StopIteration 
d = dou(b)
myiter = iter(d)
for x in myiter:
    print(x)

        
