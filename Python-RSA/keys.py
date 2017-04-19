import rsa
import math
import time
import numpy as np
if __name__ == '__main__':
    
    
    # change h for how many p's and q's you want to generate

    w = 2 # 2 columns, col 1 = p and col 2= q
    h = 1000 #sets the number of keys too be generated
    Matrix = [[0 for x in range(w)] for y in range(h)] #define matrix size to hold p's and q's
    total_bit_diff = 0
    key_size = 1024 #128 bits by default


    # Generate p's and q's and store them into the matrix
    # t0 = time.time()
    # for x in xrange(h):
        (p, q) = rsa.key.find_p_q(key_size)
        Matrix[x][0] = p
        Matrix[x][1] = q
    print (str(time.time() - t0) + " seconds to generate " + str(h) + " keys with key size of " + str(key_size))
    

    # # # print bit difference of each p and q, and the average bit difference of p and q
    for x in xrange(h):
        p_bit_length = Matrix[x][0].bit_length()
        q_bit_length = Matrix[x][1].bit_length()
        bit_diff = abs(p_bit_length - q_bit_length)
        print bit_diff
    

    
    # Each row of array : [public key encryption exp., public key mod., private key decryption exp., private key mod.]
    num_col = 4 # 4 columns defined above
    arr = [[0 for x in range(num_col)] for y in range(h)]
    for x in xrange(h):
        (pub_key, priv_key) = rsa.key.newkeys(key_size)
        arr[x][0] = pub_key.e
        arr[x][1] = pub_key.n
        arr[x][2] = priv_key.d
        arr[x][3] = priv_key.n
        print("Public Key Exp. = " + str(pub_key.e) + " Public Key Mod. = " + str(pub_key.n) + '\n')
        print("Private Key Exp. = " + str(priv_key.d) + " Private Key Mod. = " + str(priv_key.n) + '\n')
        print("---------------------------------------------------------------------------------------")
    # Check the uniqueness of the mod
    count = 0
    for x in xrange(h):
        if(arr[x][1] == arr[x][3]):
            temp_mod = arr[x][1] 
            for i in range(x+1, h):
                if(temp_mod == arr[i][1] or temp_mod == arr[i][3]):
                    count = count + 1
                    print("Modulus are not unique" + '\n')
        else:
            count = count + 1
            print("Modulus are not unique" + '\n')
    print("Modulus checking complete. " + str(count) + " moduli the same"  '\n')   
        