# Generation of Key Pairs and Encrypting/Decrypting messages
import rsa
if __name__ == '__main__':
	(bob_publicKey, bob_privateKey) = rsa.newkeys(1024)	#Step 1 
	message = "Hey Bob!".encode('utf8')					#Step 2
	ciphertext = rsa.encrypt(message, bob_publicKey)	#Step 3
	plaintext = rsa.decrypt(ciphertext, bob_privateKey)	#Step 4
	print(plaintext.decode('utf8'))						#Step 5
	


