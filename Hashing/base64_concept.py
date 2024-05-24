import base64

text_list = [b'Hello',b'Hel',b'He',b'Hello there',b'Hello How are you this is a monkey typing on a @#!xds3dy3j']


def b64_en_de(text:str):
    print()
    print(f'origional message: {text}')
    result = base64.b64encode(text)
    print(f'encoded message: {result}')
    decoded = base64.b64decode(result)
    print(f'decoded message: {decoded}')

if __name__ == '__main__':
    for i in text_list:
        b64_en_de(i)
