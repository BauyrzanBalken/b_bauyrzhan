class Person:
    def __init__(sel,name,age,school):
        sel.name = name
        sel.age = age
        sel.school = school
    
    def myfin(sel):
        print("Hello my brother " + sel.name)
    def myage(sel):
        print(sel.age + sel.school)

#p1 = Person("Bauyrzhan",15,143)
p2 = Person("Torezhan",13,167)
p2.age = int(input())
p2.myfin()
p2.myage()

print(p2.name,p2.age,p2.school)