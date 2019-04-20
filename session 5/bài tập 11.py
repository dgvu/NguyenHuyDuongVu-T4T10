        
while True:
    x = input("cho tháng  là ?")
    if x in [ "1" , "3" , "5" , "7" , "8" , "10" , "12" , "4" , "6" , "9" , "11" , "2" ]:
        if x in [ "1" , "3" , "5" , "7" , "8" , "10" , "12"]:
            print("có 31 ngày")
            break
        elif int(x) == 2:
            print("có 28 hoặc 29 ngày")
            break
        elif x in [ "4" , "6" , "9" , "11"]:
            print("có 30 ngày")
            break
        else:
            print("nhập lại số")
            break