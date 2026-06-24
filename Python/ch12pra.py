class TWOD:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class THREED(TWOD):
    def __init__(self, x, y, z):
        super().__init__(x, y) # calling the constructor of the parent class TWOD to initialize x and y
        self.z = z
    def getinfo(self):
        print(f"The vector is {self.x}i + {self.y}j + {self.z}k")

v = THREED(1, 2, 3)
v.getinfo()



class employee:
    salary = 120
    increment = 5
    @property
    def salaryafterincrement(self):
        return (self.salary * self.increment)/100 + self.salary

    @salaryafterincrement.setter
    def salaryafterincrement(self, salary):
        self.increment = ((salary/self.salary-1) * 100)

a = employee()
print(a.salaryafterincrement)
print(a.salary)
a.salaryafterincrement = 126
print(a.salary)
print(a.increment)



# METHOD 1

class complex:
    def __init__(self, real, imag):
        self.real = real
        self.img = imag

a= complex(int(input("Enter the real part of the first complex number: ")), int(input("Enter the imaginary part of the first complex number: ")))
b= complex(int(input("Enter the real part of the second complex number: ")), int(input("Enter the imaginary part of the second complex number: ")))
X= input("Enter the operation you want to perform on the complex numbers (A for addition, M for multiplication): ")
if X == "A":
    real = a.real + b.real
    img = a.img + b.img
    print(f"The sum of the complex numbers is {real} + {img}i")

elif X == "M":
    real = a.real * b.real - a.img * b.img
    img = a.real * b.img + a.img * b.real
    print(f"The product of the complex numbers is {real} + {img}i")

else:
    print("Invalid input")



#METHOD 2

class complex:
    def __init__(self, real, imag):
        self.real = real
        self.img = imag

    def __add__(self, other):
        real = self.real + other.real
        img = self.img + other.img
        return complex(real, img)
    def __mul__(self, other):
        real = self.real * other.real - self.img * other.img
        img = self.real * other.img + self.img * other.real
        return complex(real, img)

a= complex(int(input("Enter the real part of the first complex number: ")), int(input("Enter the imaginary part of the first complex number: ")))
b= complex(int(input("Enter the real part of the second complex number: ")), int(input("Enter the imaginary part of the second complex number: ")))
X= input("Enter the operation you want to perform on the complex numbers (A for addition, M for multiplication): ")
if X == "A":
    result = a + b
    print(f"The sum of the complex numbers is {result.real} + {result.img}i")

elif X == "M":
    result = a * b
    print(f"The product of the complex numbers is {result.real} + {result.img}i")

else:
    print("Invalid input")



class vector:
    def __init__(self,L):
        self.L = L  # this is a list which contains the components of the vector
    
    def __len__(self):
        return len(self.L) # this is the number of components of the vector
    
V= vector([1, 2, 3])
print(len(V)) # this will print the number of components of the vector V which is 3 because it is a 3D vector with components 1, 2 and 3