import rsa
import math
import time

if __name__ == '__main__':
    
    
    # change h for how many p's and q's you want to generate

    w = 2 # 2 columns, col 1 = p and col 2= q
    h = 1000 #sets the number of keys too be generated
    Matrix = [[0 for x in range(w)] for y in range(h)] #define matrix size to hold p's and q's
    total_bit_diff = 0
    key_size = 128 #128 bits by default


    # Generate p's and q's and store them into the matrix
    t0 = time.time()
    for x in xrange(h):
        (p, q) = rsa.key.find_p_q(key_size)
        Matrix[x][0] = p
        Matrix[x][1] = q
    print (str(time.time() - t0) + " seconds to generate " + str(h) + " keys with key size of " + str(key_size))
    

    # print bit difference of each p and q, and the average bit difference of p and q
    for x in xrange(h):
        p_bit_length = Matrix[x][0].bit_length()
        q_bit_length = Matrix[x][1].bit_length()
        bit_diff = abs(p_bit_length - q_bit_length)
        print bit_diff

    # for x in xrange(h):
        
    #     print(Matrix[x][0]) 
    #     print(Matrix[x][1])
    # 