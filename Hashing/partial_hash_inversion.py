

import hashlib as hsh
import random
import math
import timeit as tim 
N_zeros = 5
string = b'hello'
counter = 0
Max_nonce = 2**32
if __name__ == '__main__':
    start_time = tim.default_timer()
    end_time = start_time
    for enum, Nonce in enumerate(range(Max_nonce)):

        test_word = f'{string}{Nonce:08x}'
        test_bytes = test_word.encode('utf-8')
        my_hash = hsh.sha256(test_bytes)
        result = my_hash.hexdigest()
        if result[:N_zeros] == '0'*N_zeros:
            print(f'got it {test_word}, {result}' )
            break

    print(f'done in {end_time-start_time:.1f}s')

