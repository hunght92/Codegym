
import turtle
t = turtle.Turtle()


turtle.bgcolor("lightcyan")

# Vẽ mặt trước ngôi nhà
t.penup()
t.goto(-700,-300)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.fd(150)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(150)
t.lt(90)
t.fd(200)
t.lt(90)
t.end_fill()

# Vẽ cửa ra vào
t.fd(100)
t.fillcolor("palegreen")
t.begin_fill()
t.lt(90)
t.fd(110)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(110)
t.end_fill()

# Vẽ mái nhà
t.penup()
t.goto(-700,-100)
t.lt(131.41)
t.fillcolor("fuchsia")
t.begin_fill()
t.fd(100)
t.rt(82.82)
t.fd(100)
t.rt(138.59)
t.fd(150)
t.end_fill()

# Vẽ mặt sau của mái nhà
t.penup()
t.goto(-550,-100)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.rt(41.41)
t.fd(100)
t.rt(117.18)
t.fd(120)
t.rt(62.82)
t.fd(100)
t.rt(117.18)
t.fd(120)
t.end_fill()


# Vẽ tường bên
t.goto(-550,-300)
t.setheading(21.41)
t.fillcolor("yellow")
t.begin_fill()
t.fd(120)
t.lt(68.59)
t.fd(200)
t.lt(111.41)
t.fd(120)
t.end_fill()

# Vẽ cửa sổ
t.penup()
t.goto(-500,-200)
t.pendown()
t.setheading(21.41)
t.fillcolor("peru")
t.begin_fill()
t.fd(30)
t.lt(68.59)
t.fd(50)
t.lt(111.41)
t.fd(30)
t.lt(68.59)
t.fd(50)
t.end_fill()

# Vẽ thân cây
t.penup()
t.goto(0,-300)
t.setheading(0)
t.fillcolor("brown")
t.begin_fill()
t.fd(40)
t.lt(90)
t.fd(90)
t.lt(90)
t.fd(40)
t.lt(90)
t.fd(90)
t.end_fill()

# Vẽ tán cây 1
t.penup()
t.goto(-40,-210)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.setheading(39.81)
t.fd(78.1)
t.rt(79.62)
t.fd(78.1)
t.end_fill()

# Vẽ tán cây 2
t.penup()
t.goto(-30,-160)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.setheading(38.66)
t.fd(64.03)
t.rt(77.32)
t.fd(64.03)
t.end_fill()

# Vẽ tán cây 3
t.penup()
t.goto(-20,-120)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.setheading(36.87)
t.fd(50)
t.rt(73.74)
t.fd(50)
t.end_fill()

# Vẽ mặt trời
t.penup()
t.goto(-250,250)
t.pendown()
t.setheading(0)
t.fillcolor("yellow")
t.begin_fill()
t.circle(35)
t.end_fill()

t.penup()
t.goto(-215,285)
t.pendown()
t.fd(50)

t.penup()
t.goto(-225.25,309.75)
t.pendown()
t.setheading(45)
t.fd(30)

t.penup()
t.goto(-250,320)
t.pendown()
t.setheading(90)
t.fd(50)

t.penup()
t.goto(-274.75,309.75)
t.pendown()
t.setheading(135)
t.fd(30)

t.penup()
t.goto(-285,285)
t.pendown()
t.setheading(180)
t.fd(50)

t.penup()
t.goto(-274.75,260.25)
t.pendown()
t.setheading(225)
t.fd(30)

t.penup()
t.goto(-250,250)
t.pendown()
t.setheading(270)
t.fd(50)

t.penup()
t.goto(-225.25,260.25)
t.pendown()
t.setheading(315)
t.fd(30)


turtle.done()