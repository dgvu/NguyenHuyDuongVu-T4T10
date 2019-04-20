while True:
    from random import randint
    a = int(randint(-100,100))
    b = int(randint(-100,100))
    x = int(randint(-50,50))
    c = a + b
    d = c + x
    print(a, "+", b, "=", d)
    e  = str(input("phương trình đúng hay sai ?"))
    if e == "đúng":
        if d == c:
            print("true")
        else:
            print("false")
            break
    elif e == "sai":
        if d == c:
            print("false")
            break
        else:
            print("true")