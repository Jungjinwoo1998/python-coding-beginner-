def sum(n):
    a=0
    b=0
    b2=0
    c1=0
    c2=0
    for i in range(1,n+1):
        a = 2*i-1
        b= 2*i
        if i % 2 ==0:
            c1=c2+a+b
           
        else:
            c1=c2+b2+a
        b2=b
        c2=c1
        
    print(c1)

sum(5)
        