import turtle

numb = input('введите количество нужных окружностей: ')
diametr = input('введите их диаметр: ')

for i in range(int(numb)):
    turtle.circle(radius=int(int(diametr)/2))
    turtle.up()
    turtle.backward(int(diametr))
    turtle.down()