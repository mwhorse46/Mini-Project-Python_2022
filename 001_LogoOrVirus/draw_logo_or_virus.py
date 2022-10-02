import turtle
ttl = turtle.Turtle()
import tkinter as tk

def ehashiq(p1,p2,d):
    
    ttl.color('cyan')
    ttl.pensize(4)
    ttl.penup()
    ttl.goto(p1,p2)
    ttl.pendown()
    ttl.pencolor('maroon')
    ttl.turtlesize(1)
    # ttl.shape('circle')
    displaay = turtle.Screen()
    displaay.screensize(canvwidth=900, canvheight=800)
    displaay.bgcolor('gold')
    displaay.title("Ashiq's Logo")
    ttl.speed(10)
    ttl.forward(150)
    ttl.backward(150)
    ttl.right(90)
    ttl.forward(150)
    ttl.left(90)
    ttl.forward(150)
    ttl.backward(150)
    ttl.right(90)
    ttl.forward(150)
    ttl.left(90)
    ttl.forward(150)
    ttl.left(90)
    ttl.forward(150)
    ttl.backward(150)
    ttl.right(90)
    ttl.forward(150)
    ttl.right(90)
    ttl.forward(150)
    ttl.right(180)
    ttl.fd(150)
    ttl.left(90)
    ttl.fd(150)
    ttl.left(90)
    ttl.fd(150)
    ttl.right(180)
    ttl.fd(150)
    ttl.right(90)
    ttl.fd(150)
    ttl.left(90)
    ttl.fd(150)
    ttl.left(90)
    ttl.forward(150)
    ttl.left(90)
    ttl.forward(290)
    ttl.penup()
    ttl.goto(0,-250)
    ttl.left(90)
    ttl.fd(50)
    ttl.pendown()
    ttl.circle(d)
    
    button2.config(state=tk.DISABLED)
    

def clicking():
    d = 270
    p=-100;q=250
    for _ in range(4):
        ehashiq(p,q,d)
        p -=5;q-=5
        d+=1
    


def drawign():
    n = 200
    ttl.speed(7)
    ttl.color('cyan')
    while n >0:
        ttl.forward(n)
        ttl.left(n)
        n -=1
    button1.config(state=tk.DISABLED)

def press():
    drawign()

if __name__ == "__main__":
    screen = turtle.Screen()
    
    screen.title("GUI+Turtle")
    screen.bgcolor("black")
    canvas = screen.getcanvas()
    
    button1 = tk.Button(canvas.master,text="Click to draw my LOGO :)".upper(),
                       font= ('consolas',10,'bold'),
                       bg='yellow',
                       fg='blue',
                       command=clicking)
    button1.pack(side=tk.LEFT)
    button2 = tk.Button(canvas.master,text="Click to draw a virus :)".upper(),
                       font= ('consolas',10,'bold'),
                       bg='yellow',
                       fg='blue',
                       state=tk.ACTIVE,
                       command=press)
    button2.pack(side=tk.RIGHT)
    headline = tk.Label(text='What Do You want to Draw ?'.upper(),
                font= ('consolas',12,'bold'),
                fg= ("cyan"),
                bg='black',
                )

    headline.pack(side=tk.BOTTOM )
    
    turtle.done()