class employee:
    language = "Py"  #This is a class variable, it is shared by all the objects of the class
    salary = 1200000 #This is a class variable, it is shared by all the objects of the class\

    def __init__(self):
        print("Creating an object. This is a constructor, it is called when an object of the class is created") # dunder method, it is called when an object of the class is created

    def getinfo(self):
        print(f"hello {self.name}, your language is {self.language} and salary is {self.salary}")
    
    @staticmethod # This is a static method, it is not bound to any object of the class and can be called using the class name
    def greet():
        print("Good morning, have a nice day!")

pratyush = employee()
pratyush.name = "Pratyush" #This is an instance or object variable, it is unique to each object of the class
print(pratyush.name, pratyush.language, pratyush.salary)

Harry = employee()
Harry.name = "Harry" #This is an instance or object variable, it is unique to each object of the class
Harry.language = "C++" #This is an instance or object variable, it is unique to each object of the class
print(Harry.name, Harry.language, Harry.salary)
Harry.getinfo() # This is how we can call a method using the class name and passing the object as an argument  
# employee.getinfo(Harry) # Same as above but using the class name and passing the object as an argument
Harry.greet()

class employee:
    def __init__(self, name, salary, language):
        self.name = name 
        self.salary = salary 
        self.language = language 

    def getinfo(self):
        print(f"hello {self.name}, your salary is {self.salary} and language is {self.language}")
    
    @staticmethod
    def greet():
        print("Good morning, have a nice day!")

pratyush = employee("Pratyush", 1200000, "Python")
pratyush.getinfo()
pratyush.greet()