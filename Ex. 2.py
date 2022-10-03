def Pnumber(number):
    a = 0
    for i in number:
        if int(i)%3 == 0:
            a+=1
    print(a)
number = input('введите 5-ти значное число: ')
Pnumber(number)