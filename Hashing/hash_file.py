
import hashlib as hsh
from os.path import dirname, realpath
DIR = dirname(realpath(__file__))

FNAME = 'zoo.jpg' 

my_bytes = None

with open(f'{DIR}/{FNAME}', 'rb') as inf_bin:
    my_bytes = inf_bin.read()

hash = hsh.sha1(my_bytes)
print(hash.hexdigest)
