from getnums import genRSAKey
from math import log
import time

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
pqdup = 0
ndup = 0
# otherFail = 0
# dFail = 0
pqset = set()
nset = set()
tim = 0
for i in range(10000):
	print(i)
	t = time.time()
	p, q, d, e, n = genRSAKey()
	tim += time.time()-t
	if (p.bit_length() == q.bit_length()):
		fail+=1
	if p in pqset: pqdup+=1
	if q in pqset: pqdup+=1
	if n in nset: ndup+=1
	pqset.add(p)
	pqset.add(q)
	nset.add(n)
	# other standard
	# if abs(p-q) <= 2**(n.bit_length()/2-100):
	# 	otherFail+=1
	# if d < isqrt(isqrt(n))//3: dFail+=1


print("same bit length", fail)
print("pqrepeats", pqdup)
print("nrepeats", ndup)
print("keygentime", tim)
# print(otherFail)
# print(dFail)