def Exerciser(x):
    try:
        print((72*int(x))-60*int(x))

    except ValueError:
        print('x не число , попробуй еще раз')
        Exerciser(x=input('впишите значаение для x: '))


mone = 60
mtwo = 72
x=input('впишите значаение для x: ')
Exerciser(x)