import names
import random
file = open("./S05_P01.json","w")

subject = ["python","C++","java","html","php"]


for i in range(1000):
    student_roll_no = random.randint(1,100)
    student_name =names.get_full_name()
    sub = random.choice(subject)
    marks = float("%.2f"%(random.random()*100))

    file.write("{} \u2774\"student_name\":'{}', \"marks\":{} , \"subject\":{} \u2775, \n".format(student_roll_no,student_name,marks,sub))

file.close();

