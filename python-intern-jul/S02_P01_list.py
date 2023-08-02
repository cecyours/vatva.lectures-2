n = int(input("Enter the size : "))

data = [];

for i in range(n):
    data.append(input("Enter the data "+str(i)+" :"))

print("------------------")

# print(data.remove("html"))
# print(data)
for i in data:
    print(i[::-1])