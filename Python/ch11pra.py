# class Programmer:
#     Comapny = "Microsoft"
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def getinfo(self):
#         print(f"The name of the programmer is {self.name} and salary is {self.salary} and company is {self.Comapny}")
#     @staticmethod
#     def greet():
#         print("Hello, welcome to the world of programming!")

# pratyush = Programmer(input("Enter the name of the programmer: "), int(input("Enter the salary of the programmer: ")))
# pratyush.getinfo()
# pratyush.greet()

# class calculator:
#     def __init__(self, num):
#         self.square = num ** 2
#         self.cube = num**3
#         self.square_root= num**(1/2)
#     def getinfo(self):
#         print(f"The square of the number is {self.square}, the cube of the number is {self.cube} and the square root of the number is {self.square_root}")

# Number = calculator(int(input("Enter a number: ")))
# Number.getinfo()\

# class demo:
#     a = 10

# o = demo()
# print(o.a) # prints the class variable a which is 10 beacuse o is an instance of the class demo and it can access the class variable a
# o.a=20
# print(o.a) # prints the instance variable a which is 20 because we have assigned a new value to the instance variable a of the object o
# print(demo.a) # prints the class variable a which is 10 because it is accessing the class variable directly