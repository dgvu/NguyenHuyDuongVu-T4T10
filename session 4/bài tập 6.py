print("how many legs does a spider have ?")
print("1.None")
print("2.4 legs")
print("3.8 legs")
print("4.12 legs")
a = 1
while True:
    x = input("you answer ?")
    print(x)
    if x.isdigit():
        if int(x) == 2:
            print("true")
            break
        elif int(x) < 1:
            print("false")
            print("thử lại")
            print("how many legs does a spider have ?")
            print("1.None")
            print("2.4 legs")
            print("3.8 legs")
            print("4.12 legs")
        elif int(x) > 4:
            print("false")
            print("thử lại")
            print("how many legs does a spider have ?")
            print("1.None")
            print("2.4 legs")
            print("3.8 legs")
            print("4.12 legs")
        else:
            print("false")
            print("thử lại")
            print("how many legs does a spider have ?")
            print("1.None")
            print("2.4 legs")
            print("3.8 legs")
            print("4.12 legs")
    else:
        print("không phải so")
        print("thử lại")
        print("how many legs does a spider have ?")
        print("1.None")
        print("2.4 legs")
        print("3.8 legs")
        print("4.12 legs")
    a += 1
    if a > 2:
        break