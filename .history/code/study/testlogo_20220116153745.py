from turtle import * 
fillcolor('red')
begin_fill()
for i in [300.200,300,200]:
    forward(i)
    circle(10,1050)
end_fill()

up()
goto(120,65)
down()
fillcolor('white')
for i in [30,120,120]:
    left(i)
    forward(100)
end_fill()
