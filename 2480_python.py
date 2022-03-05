#틀림 ㅋㅋ
n1, n2, n3 = map(int, input().split())

if n1==n2 :
    if n2==n3 :
        reward = 10000 + n1 * 1000
    else :
        reward = 1000 + n1 * 100

elif n1==n3 :
    if n1==n2 :
        reward = 10000 + n1 * 1000
    else :
        reward = 1000 + n1 * 100

else :
    if n2==n3 :
        reward = 1000 + n1 * 100
        
    else :
        if n1 >  n2 :
            if n2 > n3 :
                reward = n1 * 100
            else :
                if n1 > n3 :
                    reward = n1 * 100
                else :
                    reward = n3 * 100
        elif n2 > n1 :
            if n1 > n3 :
                reward = n2 * 100
            else :
                if  n2 > n3 :
                    reward = n2 * 100
                else :
                    reward = n3 * 100

print(reward)
