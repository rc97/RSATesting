import rsa
import math

if __name__ == '__main__':
    
    
    # change h for how many p's and q's you want to generate
    w = 2
    h = 1000
    Matrix = [[0 for x in range(w)] for y in range(h)]
    total_bit_diff = 0

    for x in xrange(1000):
        (p, q) = rsa.key.find_p_q(128)
        Matrix[x][0] = p
        Matrix[x][1] = q

    # print bit difference of each p and q, and the average bit difference of p and q
    for x in xrange(1000):
        p_bit_length = Matrix[x][0].bit_length()
        q_bit_length = Matrix[x][1].bit_length()
        bit_diff = abs(p_bit_length - q_bit_length)
        print bit_diff
