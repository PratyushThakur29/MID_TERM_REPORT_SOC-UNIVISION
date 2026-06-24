i=1

while(i<51):
    print(i)
    i=i+1 #i+=1 can also be used

a=0
L=["harry","naveen","pratyush","krish"]

while(a<len(L)):
    print(L[a])
    a=a+1
for b in range (0,100,4): #range function(0,n-1)
    print(b)

#for loop in list, tupple, strings
l=[23,"hello",47,True]
for i in l:
    print(i)

t=(47,"pratyush","naveen")
for i in t:
    print(i)

s="Pratyush"
for i in s:
    print(i)
else:
    print("done")

for i in range(69):
    if(i==67):
        break #completely stops the function
    print(i)

for i in range(69):
    if(i==67):
        continue #skip this iteration
    print(i)

for i in range(69):
    pass #pass the function, used when u want to put the function on hold

i=0
while(i<23):
    print(i)
    i=i+1