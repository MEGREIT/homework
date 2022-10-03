from turtle import *
speed (2)

#grass 
bgcolor("green")

#sky
penup()
goto(-400, -100)
pendown()
color("darkblue")
begin_fill()
for i in range(2):
    forward(800)
    left(90)
    forward(500)
    left(90)
end_fill()


