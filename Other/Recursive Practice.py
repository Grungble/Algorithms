def do_cursing(num:int):
    if num<1:
        print('done')
        return
    
    print("pre-process",num)
    num = num -1
    do_cursing(num)
if __name__ == '__main__':
    do_cursing(10)
