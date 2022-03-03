year = int(input(""))

n = year%4

if n==0 :
    a = year%100
    b = year%400
    if a==0 :
        if b==0 :
            print("1")
        else :
            print("0")
    else :
        print("1")
else:
    print("0")
