a, b = map(int, input().split())
c = int(input())

if (a<=23)|(a>=0) :
    if (b<=59)|(b>=0) :
        if (c<=1000)|(c>=0) :
            b = b+c
            while(b>59) :
                b -= 60
                a += 1
                
            if a>=24 :
                a -= 24
                print(a,b)
            else :
                print(a,b)
