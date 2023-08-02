l=int(input("enter the size of list:"))

data=[]

for i in range(l):
    data.append(input("enter the data :"))

print(data)

for i in data:
    print(i.replace('a',''))