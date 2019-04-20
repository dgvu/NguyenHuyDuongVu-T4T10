while True:
    print("ÔN TẬP VỀ CRUD")
    a = input("chọn phần bạn muốn ôn tập ?")
    items = ["sport", "LOL", "BTS", "toán"]
    print(items)
    if a == "C":
        x = input("thứ bạn thích là ? ")
        items.append(x)
        print(items)
        break
    if a == "R":
        x = len(items)
        for i in range(x):
            print(items[i])
        break
    if a == "U":
        i = int(input("vị trí muốn đổi ?"))
        x = str(input("bạn muốn đổi thành ?"))
        remplacing_item = x
        items[i] = remplacing_item
        print(items)
        break
    if a == "D":
        i = int(input("vị trí bạn muốn xóa ?"))
        items.pop(int(i))
        print(items)
        break