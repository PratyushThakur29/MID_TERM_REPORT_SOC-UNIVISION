with open("myfile.txt", "r") as f:
    data = f.read()
    print(data)

f = open("newfile.txt", "w")
t= "i am a new file"
f.write(t)
f.close()

f = open("myfile.txt")
data = f.readline()
while(data != ""):
    print(data)
    data = f.readline()
f.close()

f = open("new2file.txt", "a")
t= "i am a new file\n"
f.write(t)
f.close()

with open("myfile.txt" , "+r") as f:
    f.write("i am a new line\n")
    f.seek(0)
    data = f.read()
    print(data)
