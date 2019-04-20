x = input("số bạn muốn thêm là : ")
a = x.split(",")
print(a)
for i in a:
    if int(i)%2 == 0:
        print(i)