#graficos.py

import turtle
p = turtle.Pen()
turtle.bgcolor("black")

p.width(3)
#              0         1          2        3           4            5
cores = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']
p.speed(0)

for x in range(300):  #0,1,2,3,4,5,6,7,8,...29
    cor = cores[x % 6]  #0,1,2,3,4,5
    p.pencolor(cor)
    p.circle(x * 5)
    p.left(60)

