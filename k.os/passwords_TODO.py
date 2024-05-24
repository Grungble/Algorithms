"""
Password system
passwords_TODO.py
using file passwords.csv
also insults.txt
"""
from os.path import dirname, realpath
import random
DIR = dirname(realpath(__file__))
import csv
import hashlib as hsh

def load_passwords( pwd_fname ):
  pwd_dict = dict()

  with open( f'{DIR}/{pwd_fname}', 'rt' ) as inf:
    next(inf)
    csvreader = csv.reader( inf )
    for row in csvreader:
      uid = row[0].strip()
      pwd = row[1].strip()
      pwd_dict[ uid ] = pwd

  return pwd_dict

def load_insults( insult_fname ):
  insults_list = [ ]
  with open(f'{DIR}/{insult_fname}', 'rt') as inf:
    for row in inf:
      new_insult = row.strip()
      insults_list.append( new_insult )
  return insults_list

def checker(password_dict:dict, insult_list:list):
  uid_input = input(f'username: ')
  pass_input = input(f'password: ')
  if password_dict.get(uid_input) == pass_input:
    print("""
        SUCCESS!

    /|  |\\            /|  |\\
    /|  |\\            /|  |\\
  / |  | \\          / |  | \\
  | |  | |          | |  | |
  \\  \\/  /  __  __  \\  \\/  /
    \\    /  / /  \\ \\  \\    /
    \\  /   \\ \\__/ /   \\  /
    \\  /   /      \\   \\  /
    _ \\ \\__/ O    O \\__/ / _
    \\\\ \\___          ___/ //
  _  \\\\___/  ______  \\___//  _
  \\\\  ----(          )----  //
  \\\\_____( ________ )_____//
    ~-----(          )-----~ _
    _____( ________ )_____  \\\\
    /,----(          )----  _//
  //     (  ______  )     /  \\
  ~       \\        /      \\  /
            \\  __  /       / /
            \\    /       / /
              \\   \\      / /
              \\   ~----~ /
                \\________/
  """)

  else:
    selected_insult = random.choice( insult_list )
    print( f'Wrong password. {selected_insult}')

if __name__=='__main__':
  FNAME = 'passwords_hashes.csv'
  password_dict =load_passwords( FNAME )
  
  FNAME2 = 'insults.txt'
  insults_list = load_insults( FNAME2 )
  checker(password_dict, insults_list)

  # TODO:
  # get input of uid and then password and authenticate the 
  # the user.
  # 
  # If they succeed, print the success
  # otherwise, insult them


  # SUCCESS

  

  # FAIL
 
  