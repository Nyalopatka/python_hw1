ticket = input("введите номер вашего билета(6 цифр): ")
if 99999 < int(ticket) < 1000000:
    res1 = int(ticket[0])+ int(ticket[1])+int(ticket[2])
    res2 = int(ticket[3])+ int(ticket[4])+int(ticket[5])
    res = res1 == res2
    if res == True:print(f"{ticket} -> yes")
    else:print(f"{ticket} -> no")
else: print(f"билета под номером {ticket} не существует")


