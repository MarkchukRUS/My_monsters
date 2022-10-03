def Method(x):
    number = ((x//15) * (x//10) + (x // 15))
    return number

x = input('впишите число x: ')
print(Method(int(x)))