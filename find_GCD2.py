def find_gcd(a,b):
    i=min(a,b)
    while True:
        if a%i==0 and b%i==0:
            return i
        i=i-1
        
print(find_gcd(200,130))
print(find_gcd(1,5))
print(find_gcd(2,18))
print(find_gcd(16,28))