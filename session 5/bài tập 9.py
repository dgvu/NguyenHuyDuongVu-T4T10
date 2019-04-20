while True:
    x = input("cho số là ?")
    if x.isdigit():
        if int(x) > 13:
            print("lớn hơn 13")
            break
        elif int(x) == 13:
            print(" bằng 13 ")
            break
        else:
            print("nhỏ hơn 13")
            break
    else:
        print("nhập lại số")