while True:
    x = input("cho số ?")
    if x.isdigit():
        from turtle import*
        shape("turtle")
        color("green")
        for i in range(100):
            forward(int(x))
            left(5)
        forward(int(x))
        
        mainloop()
        break
    else:
        print("nhập lại số")