def sum(n):
    a=0
    b=0
    b2=0
    c1=0
    c2=0
    c1_t=0
    c2_t=0
    if n%2==0:
        m=n//2
    else:
        m=n//2+1

    for i in range(1,m+1):
        a = 2*i-1
        b= 2*i
        c1=c1_t+b2+a
        c2=c2_t+a+b
        b2=b
        c2_t=c2
        c1_t = c1

        print('c1 = ',c1)
        print('c2 = ',c2)
        
        
    if n%2==0:
        print("The result is", c2)
    else:
        print("The result is", c1)
            
sum(4)
sum(5)