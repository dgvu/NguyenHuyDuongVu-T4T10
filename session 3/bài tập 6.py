a = int(input("cho a là bao nhiêu ?"))
b = int(input("cho b là bao nhiêu ?"))
c = int(input("cho c là bao nhiêu ?"))

if a == 0:
    print("phương trình bậc 1")
    if b == 0:
        if c == 0:
            print("phương trình vô số nghiệm")
        if c != 0:
            print("phương trình vô nghiệm")
    if b != 0:
        x = -c/b
        print(x)
if a != 0:
    delta = b**2 -4*a*c 
    print(int(delta))

    if delta < 0:
        print("phương trình vô nghiệm")
    elif delta == 0:
        print("phương trình có nghiệm kép")
        x = -b/a
        print(x)
    else:
        print("phương trình có 2 nghiệm phân biệt")
        x1 = (-b-(delta**1/2))/2*a
        x2 = (-b+(delta**1/2))/2*a
        print(x1)
        print(x2)