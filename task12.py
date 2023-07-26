import random
num1 = random.randint(0,1001)
num2 = random.randint(0,1001)
print(f"сумма чисел х у = {num1+num2}")
print(f"произведение чисел х у = {num1*num2}")
for i in range(1000):
    for n in range(1000):
        if num1*num2 == i*n and num1 + num2 == i+n:
            print(i,n)
            break

    


