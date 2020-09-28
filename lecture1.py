a=int(input())
b=int(input())
x=int(input())
import math
x=(x*math.pi)/180
print(math.sqrt(a**2+b**2-2*a*b*math.cos(x)))
