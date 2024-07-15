
from base64 import b64decode
from os.path import dirname, realpath
DIR = dirname(realpath(__file__))

if __name__ == '__main__':
    IFNAME = 'pmo.b64'
    OFNAME = 'result.jpg'

    with open(f'{DIR}/{IFNAME}', 'rb') as inf,\
    open(f'{DIR}/{OFNAME}', 'wb') as outf:
        b64_data = inf.read()
        result = b64decode(b64_data)
        outf.write(result)
