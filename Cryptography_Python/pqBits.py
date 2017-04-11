from getnums import genRSAKey
from math import log

fail = 0
otherFail = 0
dFail = 0
for i in range(100):
	p, q, d, e, n = genRSAKey()
	if (p.bit_length() == q.bit_length()):
		fail+=1
	# other standard
	if abs(p-q) <= 2**(n.bit_length()/2-100):
		otherFail+=1
	if d < n/4: dFail++


print(fail)
print(otherFail)
print(dFail)