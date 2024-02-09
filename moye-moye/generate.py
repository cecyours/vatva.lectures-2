
import os
import random
import time
n = random.randint(100,120)
while n:
    n-=1
    file = open("./data.txt","a+")
    file.write("hello World")
    file.close()
    os.system("gdone")
    time.sleep(10)

