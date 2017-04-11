from getnums import genRSAKey
from math import log

# def isqrt(n):  
#     'isqrt(n)\n\nReturn floor(sqrt(n)).'  
  
#     if not isinstance(n, int):  
#         raise TypeError('an int is required')  
#     if n < 0:  
#         raise ValueError('math domain error')  
  
#     guess = (n >> n.bit_length() // 2) + 1  
#     result = (guess + n // guess) // 2  
#     while abs(result - guess) > 1:  
#         guess = result  
#         result = (guess + n // guess) // 2  
#     while result * result > n:  
#         result -= 1  
#     return result  

fail = 0
# otherFail = 0
# dFail = 0
for i in range(100):
	p, q, d, e, n = genRSAKey()
	if (p.bit_length() == q.bit_length()):
		fail+=1
	# other standard
	# if abs(p-q) <= 2**(n.bit_length()/2-100):
	# 	otherFail+=1
	# if d < isqrt(isqrt(n))//3: dFail+=1


print(fail)
# print(otherFail)
# print(dFail)