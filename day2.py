list = []

n = int(input("How many items do you want to enter? "))
min = 0
max = 0

for i in range(n):
    item = int(input(f"Enter item {i + 1}: "))
    list.append(item)
print(list)

for j in list:
    min=j
    max=j
    

for k in list:
    if(k<min):
        min = k

for l in list:
    if(l>max):
        max = l
print(min, max)