a = ["blue", "red", "teal", "green"] 

from turtle import*
shape("turtle")
for i in a:
    color(i)
    forward(100)
    left(0)

mainloop()