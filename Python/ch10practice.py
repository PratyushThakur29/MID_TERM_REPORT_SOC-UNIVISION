# Q1)
# with open("poem.txt") as f:
#     k=f.read()
#     print(k)
#     if("twinkle" in k):
#         print("yes")
#     else: print("no")

# Q2)
# import random

# def game():
#     score = random.randint(1,64)
#     with open("hiscore.txt") as a:
#         b=int(a.read())
#         if(b<score):
#             with open("hiscore.txt","w") as c:
#                 c.write(str(score))
#         print(f"your score : {score}")
#     with open("hiscore.txt") as z:
#         print(f"highest score : {z.read()}")
#     return score
# game()

#  Q3)
# words = ["donkey","nigga"]
# c=""
# for word in words:
#     with open("censor.txt") as a:
#         b=a.read()
#         c=b.replace(word , "####")
#     with open("censor.txt","w") as a:
#         a.write(c)

# Q4
# with open("log.txt") as a:
#     b=a.readlines()

# line=1
# for x in b:
#     if("python" in x):
#         print(f"Yes python is present at {line}")
#         break
#     line+=1
# else: print("python is not present in log")

