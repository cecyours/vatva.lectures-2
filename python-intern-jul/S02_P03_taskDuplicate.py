n = int(input("Enter the size : "))

data = [];

for i in range(n):
    data.append(input("Enter the data "+str(i)+" :"))

# remove dublicate

print(data)
data = list(set(data)) 
print(data)