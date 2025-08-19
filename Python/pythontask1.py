def is_prime(n):
    if n<1:
        return False
    if n==1:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True

number=int(input("Enter a number: "))
sum=0
for i in range(1,number+1):
    if is_prime(i):
        sum=sum+i
    
print(sum)