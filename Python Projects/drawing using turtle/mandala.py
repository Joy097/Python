import turtle

t=turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("white")
t.speed(0)
c = 0
d=0
while True:
    for i in range(4): # 4 times will give a square
      t.forward(80)  #goes forward for 80
      t.right(90)    #rotates 90 degree
    t.right(5)
    c+=1
    if c>=390/5:
      t.forward(50)
      c=0
      d+=1
      if d>=12:
        break
t.hideturtle()
turtle.done()