from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

def genRSAKey(pe=65337, ks=2048):
	privateKey = rsa.generate_private_key(public_exponent=pe, key_size=ks, backend=default_backend())
	publicKey = privateKey.public_key()
	privateNums = privateKey.private_numbers()
	publicNums = publicKey.public_numbers()
	p = privateNums.p
	q = privateNums.q
	d = privateNums.d
	e = publicNums.e
	n = publicNums.n
	return (p, q, d, e, n)

if __name__ == '__main__':
	for i in range(5):
		print(genRSAKey())