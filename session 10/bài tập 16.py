a = {
    "HP" : [20, 600],
    "DELL" : [50, 650],
    "MACBOOK" : [12, 12000],
    "ASUS" : [30, 400],
    "ACER" : [20, 350],
    "TOSHIBA" : [10, 600],
    "FUJITSU" : [15, 900],
    "ALIENWARE" : [5, 1000]
}
print(a)
x = input("máy tính bạn muốn mua là ? ")
y = int(input("số lượng ? "))
print("sản phẩm bạn muốn mua là ", x.upper())
print("tổng số tiền phải trả là ", y*a[x.upper()][1])
z = a[x.upper()][0] - y 
a[x.upper()][0] = z
print(a)