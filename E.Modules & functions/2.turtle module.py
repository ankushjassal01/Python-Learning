"""turtle used to draw a graphics/make graphic game type or for drawing
Turtle graphics is a popular way for introducing programming to
kids. It was part of the original Logo programming language developed
by Wally Feurzig and Seymour Papert in 1966.

Imagine a robotic turtle starting at (0, 0) in the x-y plane. After an ``import turtle``, give it
the command turtle.forward(15), and it moves (on-screen!) 15 pixels in
the direction it is facing, drawing a line as it moves. Give it the
command turtle.right(25), and it rotates in-place 25 degrees clockwise.

By combining together these and similar commands, intricate shapes and
pictures can easily be drawn."""

from turtle import forward, right
import turtle
forward(100)
right(270)
forward(200)
turtle.circle(50)
right(207)
forward(223.6)
turtle.circle(50)
turtle.done()  # instead of time.sleep we can use this method. it make screen pop remain until we close the popup screen

# time.sleep(2)  # let the screen freeze/stay/visible for second defined in it.
'''
turtle methods below: 
Canvas
Pen
RawPen
RawTurtle
Screen
ScrolledCanvas
Shape
TK
TNavigator
TPen
Tbuffer
Terminator
Turtle
TurtleGraphicsError
TurtleScreen
TurtleScreenBase
Vec2D
addshape
back
backward
begin_fill
begin_poly
bgcolor
bgpic
bk
bye
circle
clear
clearscreen
clearstamp
clearstamps
clone
color
colormode
config_dict
deepcopy
degrees
delay
distance
done
dot
down
end_fill
end_poly
exitonclick
fd
fillcolor
filling
forward
get_poly
get_shapepoly
getcanvas
getmethparlist
getpen
getscreen
getshapes
getturtle
goto
heading
hideturtle
home
ht
inspect
isdown
isfile
isvisible
join
left
listen
lt
mainloop
math
mode
numinput
onclick
ondrag
onkey
onkeypress
onkeyrelease
onrelease
onscreenclick
ontimer
pd
pen
pencolor
pendown
pensize
penup
pos
position
pu
radians
read_docstrings
readconfig
register_shape
reset
resetscreen
resizemode
right
rt
screensize
seth
setheading
setpos
setposition
settiltangle
setundobuffer
setup
setworldcoordinates
setx
sety
shape
shapesize
shapetransform
shearfactor
showturtle
simpledialog
speed
split
st
stamp
sys
textinput
tilt
tiltangle
time
title
towards
tracer
turtles
turtlesize
types
undo
undobufferentries
up
update
width
window_height
window_width
write
write_docstringdict
xcor
ycor

'''
