# Multiple Inheritance

class employee:
    company = "Google"
    def getinfo(self):
        print(f"The company name is {self.company}")

class Coder:
    language = "Python"
    def getlanguage(self):
        print(f"The language is {self.language}")

class programmer(employee, Coder): # multiple inheritance
    def getinfo1(self):
        print(f"The company name is {self.company} and the language is {self.language}")

pratyush = programmer()
pratyush.getinfo()
pratyush.getlanguage()
pratyush.getinfo1()

# Multilevel Inheritance

class employee:
    company = "Google"
    def getinfo(self):
        print(f"The company name is {self.company}")

class Coder(employee):
    language = "Python"
    def getlanguage(self):
        print(f"The language is {self.language}")

class programmer(Coder): # multiple inheritance
    def getinfo1(self):
        print(f"The company name is {self.company} and the language is {self.language}")

pratyush = programmer()
pratyush.getinfo()
pratyush.getlanguage()
pratyush.getinfo1()

# Another simple example of multilevel inheritance

class A:
    a=1
class B(A):
    b=2
class C(B):
    c=3
o = A()
print(o.a) # prints 1 because it is accessing the class variable a of class A   
o1 = B()
print(o1.a) # prints 1 because it is accessing the class variable a of class A through class B
print(o1.b) # prints 2 because it is accessing the class variable b of class B
o2 = C()
print(o2.a) # prints 1 because it is accessing the class variable a of class A through class C
print(o2.b) # prints 2 because it is accessing the class variable b of class B through class C
print(o2.c) # prints 3 because it is accessing the class variable c of class C

class A:
    def __init__(self):
        print("This is constructor of class A")
    a=1
class B(A):
    def __init__(self):
        print("This is constructor of class B") 
    b=2
class C(B):
    def __init__(self):
        super().__init__() # this will call the constructor of class B but not of class A because the base class of class C is class B and not class A
        print("This is constructor of class C")
    c=3
o = A() # this will call the constructor of class A
o1 = B() # this will call the constructor of class B
o2 = C() # this will call the constructor of class C and then class B

class employee:
    a=1

    @classmethod # this is a class method which can access the class variable a and it takes the class as the first parameter by convention we use cls as the first parameter of a class method
    def show(cls):
        print(f"The value of a is {cls.a}")

    @property # this is a property decorator which is used to create a property which can be accessed like an attribute but it is actually a method
    def name (self):
        return f"{self.fname} {self.lname}"
    
    @name.setter # this is a setter method which is used to set the value of the property name
    def name(self, name):
        self.fname = name.split()[0] # this will split the name into first name and last name and assign the first name to fname
        self.lname = name.split()[1] # this will split the name into first name and last name and assign the last name to lname

e=employee()
e.a=45
print(e.a) # this will print 45 because we have assigned a new value to the class variable a of the object e
e.show() # this will print the value 1 because the class method show is accessing the class variable a of the class employee and not the instance variable a of the object e
e.name = "Pratyush Kumar" # this will call the setter method of the property name and set the value of fname and lname
print(e.name) # this will call the getter method of the property name and return the value

class Student:
    def __init__(self, marks):
        self._marks = marks          # _marks = private by convention

    @property                        # GETTER — called when you READ e.grade
    def grade(self):
        if self._marks >= 90:
            return "A"
        elif self._marks >= 75:
            return "B"
        else:
            return "C"

    @property                        # GETTER — read computed value like attribute
    def marks(self):
        return self._marks

    @marks.setter                    # SETTER — called when you WRITE e.marks = 85
    def marks(self, value):
        if value < 0 or value > 100:
            print("Marks must be between 0 and 100")
        self._marks = value          # validation before setting

    @marks.deleter                   # DELETER — called when you DEL e.marks
    def marks(self):
        print("Marks deleted!")
        del self._marks              # removes the attribute

s = Student(85)

# GETTER in action
print(s.marks)     # 85  → calls @property (getter)
print(s.grade)     # B   → another getter, computes from _marks

# SETTER in action
s.marks = 95       # calls @marks.setter → validates, then stores
print(s.marks)     # 95
print(s.grade)     # A

# SETTER validation
s.marks = -10      # ❌ raises ValueError: Marks must be between 0 and 100

# DELETER in action
del s.marks        # calls @marks.deleter → prints "Marks deleted!"

class Number:
    def __init__(self, n):
        self.num=n
    def __add__(self, other): # this is a magic method which is used to overload the + operator
        return self.num + other.num
num1 = Number(5)
num2 = Number(10)
print(num1 + num2) # this will call the __add__ method of the class Number and return the sum of the two numbers which is 15

p1=6
p2=4
p3=p1//p2
print(p3)