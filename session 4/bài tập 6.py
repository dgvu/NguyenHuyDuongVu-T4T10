print("how many legs does a spider have ?")
print("1.None")
print("2.4 legs")
print("3.8 legs")
print("4.12 legs")
a = 1
while True:
    x = input("you answer ?")
    print(x)
    if x in [ "1" , "2", "3" ,"4" ]:
        if int(x) == 2:
            print("true")
            break
        else:
            print("false")
            print("thử lại")
    else:
        print("không phải so")
        print("thử lại")
    a += 1
    if a > 2:
        break