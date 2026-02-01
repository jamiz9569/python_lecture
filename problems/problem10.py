# oops concepts
#question1
class programmer:
    def __init__(name,dept,role,developer):
        name.name=name
        name.dept=dept
        name.role=role
        name.developer=developer
    def info(name):
        print(f"Name of the programmer is {name.name}")
        print(f"Department of the programmer is {name.dept}")
        print(f"Role of the programmer is {name.role}")
        print(f"Developer of the programmer is {name.developer}")
    
p1=programmer("Alice","IT","Backend Developer","Python")
p1.info()

#question2
class square:
    def __init__(self, num):
        self.num=num
    def square(self):
        return self.num*self.num
    def cube(self):
        return self.num*self.num*self.num
    def squareroot(self):
        return self.num**0.5
    s1=square(4)
    print("Square is:",s1.square())
    print("Cube is:",s1.cube())
    print("Square root is:",s1.squareroot())

#question3
class Test:
    a = 5   # class attribute

obj = Test()
obj.a = 0  # creates an instance attribute
print(Test.a)  # 5
print(obj.a)   # 0
