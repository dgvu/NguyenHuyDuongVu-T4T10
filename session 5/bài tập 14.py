while True:
    y = input("tên tài khoản là ?")
    x = input("mật khẩu là ?")
    a = input("nhập lại mật khẩu")
    z = input("email là ?")
    print(y)
    print(x)
    print(z)
    check_x = 0
    for i in x:
        if i.isdigit():
            check_x = 1
    if  check_x == 1:
        if len(x) < 8:
            print("mật khẩu không đủ điều kiện nhập lại mật khẩu")
        else:
            if x != a:
                print("mật khẩu không khớp, yêu cầu nhập lại ")
            else:
                if "@" in z:
                    print("ok")
                    break
                else:
                    print("email ko hop le")
    else:
        print("yêu cầu mật khẩu phải có ít nhất mội chữ số")