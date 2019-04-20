x = input("tên tài khoản là ?")
y = input("mật khẩu là ?")
a = input("nhập lại mật khẩu")
z = input("email là ?")

print(x)
print(y)
print(z)
while True:
    if y != a:
        a = input("nhập lại mật khẩu")
    else:
        break
    