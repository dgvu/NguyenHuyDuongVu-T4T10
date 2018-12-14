while True:
    x = input("nhập tên của bạn ?")
    print(x)
    if x.isalpha():
        print("nhập chữ")
        break
    else:
        print("không phải chữ")