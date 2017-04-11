from getnums import genRSAKey

fails = 0
for i in range(10):
	p, q, d, e, n = genRSAKey(17, 10)
	print(p, q, d, e, n)