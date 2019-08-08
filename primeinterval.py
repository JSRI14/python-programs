a,b=map(int,input().split())

for n in range(a,b+1):
    c=0
    for i in range(2,n+1):
        if(n%i==0):
            c+=1
    if c==1:
        print(n)



