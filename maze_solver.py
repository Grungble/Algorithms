from os.path import realpath, dirname
import csv

DIR = dirname(realpath(__file__))


def read_maze( in_filename: str ) -> list :
  """
  read the maze from an incoming file
  returns a 2D list of ints, 
  1 for wall
  0 for no wall
  """
  in_maze = [ ]

  with open( ifname, 'rt' ) as inf:
    csvreader = csv.reader( inf )
    for row in csvreader:
      new_row = [ int(i) for i in row ]
      in_maze.append( new_row )
  
  return in_maze


def display_maze( imaze: list ):
  """
  TODO: display the maze 
  can use simply 1s and 0s or can
  use glyphs to represent walls/no walls  
  """
  print( 'not yet implemented' )
  pass




def solve_maze( location: tuple, maze: list ):
  """
  TODO: solve the maze.
  NOTE: may need to adjust function signature for
  necessary parameters
  location : 2-tuple representing current row, col of the player
  maze: 2D list representing the maze
  """
  print( 'not yet implemented' )
  pass
  

# 
# MAIN
# 
if __name__=='__main__':
  mazename = 'maze.csv'
  ifname = f'{DIR}/{mazename}'
  my_maze = read_maze( ifname )

  display_maze( my_maze )

  start = (0,1)
  solve_maze( start, my_maze )
