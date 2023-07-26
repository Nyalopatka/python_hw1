chislo = input("введите 3-х значное число:")   #не сделал int(input()) т.к пишет ошибку  
                                               #Traceback (most recent call last):
                                               #  File "c:/C#/work/Новая папка (9)/python/task2.py", line 3, in <module>
                                               #    res = chislo[0]+chislo[1]+chislo[2]
                                               #TypeError: 'int' object is not subscriptable
if 99 < int(chislo) < 1000:
    res = int(chislo[0])+int(chislo[1])+int(chislo[2])
    print(f"{chislo} -> {res} ({chislo[0]} + {chislo[1]} + {chislo[2]})")
else:
    print(f"ошибка {chislo} не является трехзначным числом")
    