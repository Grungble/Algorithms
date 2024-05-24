
import hashlib as hsh
from os.path import dirname, realpath
my_msg = ['Hello','hello','helo','hell',
'Hello, my name is Sam Francisco and I am an alien who just loves to eat pizza and chocklit sauce. Ninja!']
def hash_thing(my_message:str):
    my_bytes = my_message.encode('utf-8')
    print(my_bytes)
    hash = hsh.sha1(my_bytes)
    print(hash.digest())
    for digest_bytes in hash.digest():
        print(f'{digest_bytes:02x}', end='')
    print()
    print(hash.hexdigest())
def hash_file():
    pass
if __name__ == '__main__':
    for msg in my_msg:
        print(msg)
        hash_thing(msg)
        print()