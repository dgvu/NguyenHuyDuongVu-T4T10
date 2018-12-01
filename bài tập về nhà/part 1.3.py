from turtle import*

shape("turtle")
color("blue")
speed(0)
for i in range(15):
    for i in range(4):
        left(90)
        forward(20)
    for i in range(4):    
        right(90)
        forward(20)
    forward(20)

mainloop()