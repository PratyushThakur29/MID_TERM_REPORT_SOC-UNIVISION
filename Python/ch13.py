# ADVANCED PYTHON NEW FEATURES

# 1 WARLUS OPPERATOR :=

if (n := len("Hello World")) > 10:
    print(f"The length of the string is {n}, which is greater than 10.")

# 2 types

n : int = 10
name: str = "Alice"

def sum(a: int, b: int) -> int:
    return a + b

print(sum(int(input("Enter a number: ")), int(input("Enter another number: "))))

# 3 

from typing import List, Tuple, Dict, Union

#list of integers
numbers: List[int] = [1, 2, 3, 4, 5]
#tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)
#dictionary with string keys and integer values
ages: Dict[str, int] = {"Alice": 30, "Bob": 25, "Charlie": 35}
#UNION of a string and an integer
data: Union[str, int] = "Hello" 

# 4 MATCH CASE STATEMENT

def status(a : int):
    match a:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case 2:
            return "Two"
        case _:
            return "Other"

print(status(int(input("Enter a number: "))))

# 5 Merge and update dictionaries

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 3} # if there are duplicate keys, the value from the second dictionary will be used in the merged dictionary
merged_dict = dict1 | dict2
print(merged_dict)

updated_dict = dict1 | {"b": 20, "e": 5}
print(updated_dict)

# 6 OPEN FILES

with(
    open("file1.txt", "r") as file1,
    open("file2.txt", "r") as file2
):
    # do something with the files

# 7 exception

try:
    x = int(input("Enter a number: "))
    print(f"The number you entered is {x}")

except ValueError:
    print("Invalid input. Please enter a valid number.")

except Exception as e:
    print(f"An error occurred: {e}") # This wont stop the program, it will just print the error message

else:
    print("No errors occurred.") # this will be printed if there are no errors in the try block

print("Thanks for using the program!") # this will be printed even if there is an error in the try block

# 8 raising an exception

a = int(input("Enter a number: "))
b= int(input("Enter another number: "))

if(b == 0):
    raise ValueError("Cannot divide by zero") # This will stop the program and print the error message "Cannot divide by zero"

else:
    print(f"The result of {a} divided by {b} is {a/b}")

# why to use finally block when we can just write the code after the try except block?
# Its main use case is in functions, where we want to run the code in the finally block regardless of return statements in the try or except blocks. If we write the code after the try except block, it will not be executed if there is a return statement in the try or except block. But if we write the code in the finally block, it will be executed even if there is a return statement in the try or except block.

def main():
    try:
        x = int(input("Enter a number: "))
        print(f"The number you entered is {x}")
        return x

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

    finally:
        print("This will always be printed, regardless of return statements in the try or except blocks.") # this will be printed even if there is a return statement in the try or except block , it overrides the return statement in the try or except block

main()

# 8 Global

a= 67
print (a)
def fun():
    global a # changes the variable globally not just in the function
    a=69
    print(a)

fun()
print(a)

# 9 enumerate

L=[2,56,4,657,3]
# index = 0
# for item in L:
#     print(f"the iteam number at index {index} is {item}")
#     index+=1

for index, item in enumerate(L):
    print(f"the iteam number at index {index} is {item}")

# 10 list compreshension

myList = [1,3,3,4,5,9]

# squaredList=[]
# for item in myList: 
#     squaredList.append(item*item)

# print(squaredList)

squaredList = [i*i for i in myList]
print(squaredList)