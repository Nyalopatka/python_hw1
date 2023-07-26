n = int(input("введите число N: "))
count = 1
while 2**count <= n:
    print(2**count)
    count+=1