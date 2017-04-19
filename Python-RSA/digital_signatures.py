# RSA for Authentication and Digital Signatures 
import rsa
if __name__ == '__main__':
	(alice_publicKey, alice_privateKey) = rsa.newkeys(1024)				#Step 1 
	message = "There's always money in the banana stand"				#Step 2
	signature = rsa.sign(message, alice_privateKey, 'SHA-512')			#Step 3
	is_Alice = rsa.verify(message, signature, alice_publicKey)			#Step 4
	print(is_Alice)
								
	


