a = []
while True:
    x = int(input("số bạn muốn thêm là ?"))
    if x != 0:
        a.append(x)
    else:
        print(a)
        print(sum(a))
        break