while True:
    x = input("cho số là ?")
    if x.isdigit():
        if int(x) < 0:
            print("nhập lại")
        else:
            for i in range(int(x)+1, -1, -1):
                print(i)
        break
    else:
        print("nhập lại")