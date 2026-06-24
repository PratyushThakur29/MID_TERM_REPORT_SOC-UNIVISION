d={}                       #empty dictonary
marks = {
   "pratyush":7 ,
   "pavan":6
}                          #dictionary
print(marks)

print(marks["pratyush"])
print(marks.update({"pratyush":8,"jahanvi":7}))
print(marks)               #dictionary are mutable
print(marks.items())
print(marks.values())
print(marks.keys())
print(marks.get("jahanvi"))
print(marks.pop("pratyush"))
print(marks)
print(marks.popitem())     #removes last item inserted
print(marks.clear)
print(marks)

e=set()    #empty set
f={1,8,2,3}
print(f) #order doesn't matter
print(f.add(4)) #sete are mutable
print(f)
print(f.remove(4))
print(f)
print(f.union({8,11}))
print(f.intersection({8,11,4}))

s1={1,4,8,12}
s2={1,3,8,10}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)