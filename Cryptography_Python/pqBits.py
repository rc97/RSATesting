from getnums import genRSAKey
from math import log

fail = 0
for i in range(100):
	p, q, d, e, n = genRSAKey()
	print(p.bit_length(), q.bit_length())
	print(int(log(p, 2)))
	print(int(log(q, 2)))
	if (p.bit_length() == q.bit_length()):
		fail+=1

print(fail)