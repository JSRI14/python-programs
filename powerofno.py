import math

n = int(input("  Enter the Integer : "))
ex = int(input("  Enter Exponent Value : "))

p = math.pow(n, ex)
    
print("The Result of {0} Power {1} = {2}".format(n, ex, p))
