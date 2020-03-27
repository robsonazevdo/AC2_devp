primos = []
for div in range(1,550+1):
    cont = 0

    for x in range(1,div+1):
        if div % x == 0:
            cont +=1
    
    if cont == 2:
        primos.append(x)

a = 0
b = 10
for j in range(1,10+1):
    for i in range(a,b):
        print(primos[i],end=',' )
    print(' --> ',b,end='\n')
    a += 10
    b += 10    




