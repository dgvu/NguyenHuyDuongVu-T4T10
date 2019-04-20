#for i in "NGUYENTHETUNG":
#    print(i)

while True:
    x = input("mật khẩu của bạn ?")
    check_x = 0
    for i in x:
        if i.isdigit():
            check_x = 1
    if  check_x == 0:
        print("false")
    elif check_x == 1:
        print("true")
        break

