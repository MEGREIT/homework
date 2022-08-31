from turtle import *
#დავხატოთ ოთკუთხედი (draw square)

speed(2)

    #კვადრატის დახატვა
shape("arrow")   
color("red")
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90) 
end_fill()
#სახურავის დახატვა 
color("black")
begin_fill()

left(90)
forward(100)
right(30)
forward(100)
right(120)
forward(100)
right(120)
forward(100)
left(90)
forward(100)
color("red")

left(90)
forward(50)
color("red")
color("black")

#კარის დახატვა 
begin_fill()

left(90)

forward(50)
right(90)
forward(20)
right(90)
forward(50)
left(90)



end_fill()
exitonclick()




