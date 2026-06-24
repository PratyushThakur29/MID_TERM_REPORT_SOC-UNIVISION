try:
    with(
        open("1.txt","r") as file1,
        open("2.txt") as file2,
        open("3   .txt") as file3
    ):
        print(file1.read(),file2.read(),file3.read())

except Exception as e:
    print(e)

L=[1,2,3,4,5,6,7,8,9,10,11]
for index, item in enumerate(L):
    if(index == 2 or index == 4 or index == 6):
        print(item)
    else:
        continue

a=int(input("Enter Number: "))

List=[a*i for i in range(1,11)]
print(List)

with open("tables.txt","a") as f:
    f.write(f"Table of {a}: {str(List) + "\n"}")


x=int(input("Enter Number1: "))
y=int(input("Enter Number2: "))

try:
    print(f"Ans: {x/y}")

except ZeroDivisionError:
    print("Ans: infinite")