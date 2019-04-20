while True:
    x = input("cho số là ?")
    if x.isdigit():
        if int(x)%2 ==0:
            print("là số chẵn")
            break
        else:
            print("là số lẻ")
            break
    else:
        print("nhập lại số")