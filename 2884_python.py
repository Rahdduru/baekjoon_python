h, m = map(int, input().split())

if (h<=23)|(h>=0) :
    if (m<=59)|(h>=0) :
        if m>=45 :
            m -= 45
            print(h,m)
        else :
            m = abs(m-45)
            m = 60-m
            if h==0 :
                h = 23
                print(h,m)
            else :
                h -= 1
                print(h,m)
