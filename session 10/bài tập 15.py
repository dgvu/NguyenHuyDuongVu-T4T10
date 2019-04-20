a = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 12000,
    "ASUS" : 400,
    "ACER" : 350,
    "TOSHIBA" : 600,
    "FUJITSU" : 900,
    "ALIENWARE" : 1000
}
print(a)
x = input("máy tính bạn muốn mua là ? ")
y = int(input("số lượng ? "))
print("sản phẩm bạn muốn mua là ", x.upper())
print("tổng số tiền phải trả là ", y*a[x.upper()])