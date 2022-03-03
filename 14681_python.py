x = int(input())
y = int(input())

if (x<=1000)|(x>=-1000) :
    if x!=0 :
        if (y<=1000)|(y>=1000) :
            if y!=0 :
                if x>0 :
                    if y>0 :
                        print("1")
                    else :
                        print("4")
                else :
                    if y>0 :
                        print("2")
                    else :
                        print("3")
