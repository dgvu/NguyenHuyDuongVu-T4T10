while True:
    x = input("mật khẩu của bạn ?")
    check_x = 0
    for i in x:
        if i.isdigit():
            check_x = 1
    if  check_x == 1:
        if len(x) < 8:
            print("false")
        else:
            if x == x.lower() or x == x.upper():
                print("false")
            else:
                print("true")
                break