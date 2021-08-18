# To find the prime number
n=int(input("enter number"))
count=0
i=1
while i<=n:
    if n%i==0:
        count=count+1
    i=i+1
if count==2:
    print("This number is prime")
else:
    print("This number is not prime")
