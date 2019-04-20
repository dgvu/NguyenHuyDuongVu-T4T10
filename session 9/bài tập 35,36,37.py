b = 0
while True:
    print("how many legs an octopus has:")
    a = {
        "1" : "One leg",
        "2" : "Two leg",
        "3" : "Four leg",
        "4" : "Eight leg",
    }
    b += 1
    for i in a:
        print(i, ".", a[i])
    x = input("your answer: ")
    if x in a:
        if x == "4":
            print("HURA!!!!")
            break
        else:
            print("Not a correct  answer")
    if b > 1 :
        break