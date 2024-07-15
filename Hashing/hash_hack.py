import csv
from os.path import dirname, realpath

DIR = dirname(realpath(__file__))
common_list = []




if __name__ == '__main__':
    ROCKNAME = 'rockyou.top500.csv'
    
    with open(f'{DIR}/{ROCKNAME}', 'ib') as rnf:
        
