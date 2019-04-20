while True:
    x = input("cho số ?")
    if x.isdigit():
        from turtle import*
        shape("turtle")
        color("green")
        for i in range(100):
            forward(100)
            left(360/int(x))
        forward(100)
        
        mainloop()
        break
    else:
        print("nhập lại số")