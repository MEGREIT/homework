from turtle import *

width(7)
speed(2)
#draw 3 different circle
color("orange")
begin_fill()
circle(30)
circle(-50)
penup()
goto(0, -100)
pendown()
circle(-100)
end_fill()

penup()
goto(0, -200)
pendown()
color("black")
circle(2)
penup()
goto(0, -230)
pendown()
circle(2)
penup()
goto(0, -170)
pendown()
circle(2)

color("black")
penup()
goto(0, -50)
pendown()
circle(2)
penup()
goto(0, -70)
pendown()
circle(2)
penup()
goto(0, -30)
pendown()
circle(2)

#draw eyes
penup()
goto(-10, 30)
pendown()
circle(1)

penup()
goto(10, 30)
pendown()
circle(1)

#draw mouth
width(4)
penup()
goto(-10, 15)
pendown()
forward(20)


width(7)
color("blue")
begin_fill()
penup()
goto(-20,57)
pendown()
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

color("red")
penup()
goto(50, -30)
pendown()
left(30)
forward(90)
circle(2)
circle(-2)

penup()
goto(-50, -30)
pendown()
right(63)
forward(90)
circle(2)
circle(-2)

color("orange")
penup()
goto(0, 0)
pendown()






exitonclick()