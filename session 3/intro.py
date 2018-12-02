yob = int(input("nam sinh cua ban ?"))
age = 2018 - yob
print(age)

if age < 6:
    print("em bé")
elif age < 18: #(nếu điều kiện trên đúng thì nó sẽ bỏ qua)
    print("thanh niên")
else:
    print("người lớn")