from Crypto.PublicKey import RSA
from Crypto import Random

def check(p, q, nlen, l):
	if (abs(p-q) > 2^nlen/2 - 100):
		l[0]+=1
	else:
		l[1]+=1

def main():
	output = [0, 0]
	pqbitcheck = [0, 0]
	randy = Random.new().read
	for i in range(1,10000):
		key = RSA.generate(1024, randy)
		check(key.p, key.q, (len(bin(key.n)) - 2), output)
		if (len(bin(key.q)) - len(bin(key.p)) > 0):
		      pqbitcheck[1]+=1
		else:
		      pqbitcheck[0]+=1
	print("Number of keys that fit the criteria: %d\/10000\n", output[0])
	print("Number of keys that do not fit: %d\/10000\n", output[1])
	print("Number of times p and q were at least a bit apart in length: %d\/10000\n", pqbitcheck[1])
	print("Number of times they weren't: %d\/10000\n", pqbitcheck[0])
	
main()