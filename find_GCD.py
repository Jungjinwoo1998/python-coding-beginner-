#최대공약수 찾기
a=[35,100]
def find_gcd(a):
    if a[0]<a[1]:
        b=a[0]
        while (a[1]%b==0 and a[0]%b==0)==False:
            b=b-1 
        return b
    else:
        b=a[1]
        while (a[0]%b==0 and a[1]%b==0)==False:
            b=b-1
        return b
print(find_gcd(a))
            
