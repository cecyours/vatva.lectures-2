l=int(input("enter size of list :"))

data=[]

for i in range(l):
    data.append(input("enter the data :"))

print(data)

if input("enter check the value :") in data:
    print("yes data in the list")
else:
    print("this data not in this list")
