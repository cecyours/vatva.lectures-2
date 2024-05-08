
import os
import random
import time
n = random.randint(500,720)
while n:
    d = random.randint(1,5)
    n-=1
    file = open("./data.txt","a+")
    file.write("hello World")
    file.close()
    os.system("gdone")
    time.sleep(d)

