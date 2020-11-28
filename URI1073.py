N=int(input())
if(N<2000):
    if(N>5):
        for x in range(1, N+1):
            if (x % 2 == 0):
                print(str(x)+"^"+str(2)+" = "+str(x**2))




