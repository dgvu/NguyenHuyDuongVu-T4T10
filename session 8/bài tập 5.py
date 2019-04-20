a = ["blue", "red", "teal", "green"] 

for i,item in enumerate(a):
    print(i + 1, ".", item)
x = input("item to delete : ")
if x.isdigit():
    b = int(x) - 1
    a.pop(b)
    for i,item in enumerate(a):
        print(i + 1, ".", item)
else:
    a.remove(str(x))
    for i,item in enumerate(a):
        print(i + 1, ".", item)