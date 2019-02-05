n1=int(input("Enter number:"))
temp=n1
rev=0
while(n1>0):
    dig=n1%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("yes")
else:
    print("no")
