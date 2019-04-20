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
for i in a:
    print(i, "Tổng giá trị của máy là ", a[i][0]*a[i][1])