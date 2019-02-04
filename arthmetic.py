a = int(input("Enter First Number: "))

b = int(input("Enter Second Number:"))


ch = input("Enter ur choice: ")



if ch == '+':
    
    c = float(a) + float(b)
    print (a, ch, b, ":", c)

elif ch == '-':
    
    c = float(a) - float(b)
    print ( a, ch, b, ":", c)

elif ch == '*':
    
    c = float(a) * float(b)
    print ( a, ch, b, ":", c)

elif ch == '/':

    if ( b == 0 ):
        print ("infinity")
else:
     
    c = float(a) / float(b)
    print (a, ch, b, ":", c)
