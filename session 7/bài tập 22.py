items = ["sport", "LOL", "BTS", "toán"]
print(*items, sep=', ')
while True:
    x = input("thứ bạn muốn thêm là ?")
    if x != "không":
        items.append(x)
    else:
        print(*items, sep=', ')
        break