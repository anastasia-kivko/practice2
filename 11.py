from turtle import *
import math

xc = float(input("xc = "))
yc = float(input("yc = "))
r = float(input("r = "))
x = float(input("x = "))
y = float(input("y = "))

distance = math.sqrt((x - xc) ** 2 + (y - yc) ** 2)

if distance == r:
    rez = "Точка на окружности"
elif distance < r:
    rez = "Точка внутри окружности"
else:
    rez = "Точка вне окружности"

speed(0)
penup()
goto(xc, yc - r)
pendown()
color("black")
circle(r)
penup()
goto(x, y)
pendown()
dot(6, "red")
penup()
goto(xc, yc - r - 25)
color("red")
write(rez, align="center", font=("Times New Roman", 11, "normal"))
hideturtle()
done()