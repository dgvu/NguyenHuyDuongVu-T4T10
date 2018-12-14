name = str(input("your username ?"))

if name != "techkids":
    print("you are not superuser")
else:
    password = str(input("your password ?"))
    
    if password != "codethechange":
        print("invalid password")
    else:
        print("welcome, superuser")