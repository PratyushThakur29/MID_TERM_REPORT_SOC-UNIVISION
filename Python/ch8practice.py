a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))
d=int(input("Enter number 4: "))

if(a>b and a>c and a>d):
    print("a is the largest no.")
elif(b>a and b>c and b>d):
    print("b is the largest no.")
elif(c>b and c>a and c>d):
    print("c is the largest no.")
elif(d>b and d>a and d>c):
    print("d is the largest no.")
else:
    print("no one word is largest")

a=int(input(" marks of subject 1: "))
b=int(input(" marks of subject 2: "))
c=int(input(" marks of subject 3: "))
d=(a+b+c)/3
if(a>33 and b>33 and c>33 and d>40):
    print("pass")
else:
    print("fail")

p1="make a lot of money"
p2="subscribe to this"

a=input("enter your comment: ")
if(p1 in a or p2 in a):
    print("this comment is a spam")
else:
    print("this comment is not a spam")

a=input("enter your name: ")
if(len(a)<10):
    print("username is valid")
else:
    print("username is not valid")

a=float(input("enter your marks: "))
if(100>=a>=90):
    print("Ex")
elif(90>a>=80):
    print("A")
elif(80>a>=70):
    print("B")
elif(70>a>=60):
    print("C")
elif(60>a>=50):
    print("D")
elif(50>a>=0):
    print("F")
else:
    print("not valid marks")

p="Harry"
a=input("enter post: ")

if(p in a):
    print("Yes the post is talking about Harry")
else:
    print("No the post is not talking about Harry")