num=int(input("enter a number"))
count=0
for i in range(2,num//2):
    if num%i==0:
        count=count+1
    else:
        count=0
if count==0:
    print("prime")
else:
    print("not prime")