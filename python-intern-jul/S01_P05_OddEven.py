
n = int(input("Enter the number : "))

for i in range(int(input("enter starting number")),n+1):
    if i%2==0:
        print(i)

print("----------------")

for i in range(1,n+1):
    if i%2!=0:
        print(i)