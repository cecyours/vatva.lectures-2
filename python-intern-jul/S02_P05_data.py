import random
import names
import time
import os

subject = ["Python","java","Html","C++","Ruby","C","Php","Kotlin","JavaScript","css","vb.NET"]

# rollNo,studentName, subject, marks, date,
data = dict()



for i in range(5):
    s_roll_no = i+1
    s_name = names.get_full_name()
    s_subject = random.choice(subject)
    s_marks = float("%.4f"%(random.random()*100))

    student = {'rollNo':s_roll_no,'name':s_name,'subject':s_subject,'marks':s_marks}
    data[str(s_roll_no)]=student
    print(".")
    time.sleep(1)
    if(i%3==0):
        # clean the screen
        os.system("clear")
        print("l")
        print("o")
        print("a")
        print("d")
        print("i")
        print("n")
        print("g")
    
    

# print(data)
os.system("clear")
# print(data['2'])
for i in data:
    print(data[i])