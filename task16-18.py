import random
nSize = int(input("введите размер списка: "))
search = int(input("введите число которое нужно найти: "))

new_list = [random.randint(1,10) for _ in range(nSize)]

count = 0
for i in range(nSize):
    if new_list[i] == search: count+=1
else:
    nearest_num = new_list[0]
    for i in range(nSize):
        if search - nearest_num > search - new_list[i]:
            nearest_num = new_list[i]
             
             
print(nSize)
print(new_list)
print(search)
if count != 0:print(count)
else:print(f"{nearest_num} -> ближайщее к {search} число")
