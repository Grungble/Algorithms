"""
CONWAY LIFE using pygame 

make sure to install pygame using pip install pygame

"""
# Import and initialize the pygame library
import pygame
import csv
from os.path import dirname, realpath

# GLOBAL CONSTANTS

DIR = dirname(realpath(__file__))

# Global defs

# how big each map grid square is
PIXEL_SIZE = 50  

# 40x40 png
# should be 10pixels smaller than PIXEL_SIZE
SPRITE_FNAME = 'pika.png'
# to center the sprite:
SPRITE_OFFSET = { 'x' : 5, 'y' : 5 }

# Main (these get init'd in init method)
MAP_SIZE = {  }
SCREEN_SIZE = {  }
RECT_SIZE = { }

def read_grid_from_csv( grid_filename ):
  """
  read the csv file and populate the grid
  """
  grid = []
  full_fname = f'{DIR}/{grid_filename}'

  with open(f'{full_fname}', 'rt') as inf:
    csvreader = csv.reader(inf)
    for row in csvreader:
      new_row = []
      grid.append( new_row)
      for col in row:
        new_row.append( int(col) )
  return grid


def count_neighbors_for_cell( grid:list, row:int, col:int ) -> int:
  """
  count all the neighbors for the cell
  at row,col
  return that value
  """
  num_neighbors = 0

  # TODO: complete this

  return num_neighbors


def do_counts( grid:list, count_grid:list ):
  """
  GIVEN
  update the neighbor grid with the current
  counts.
  note: we will exclude the outside cells
  from our calculations for ease
  """
  START_ROW = 1
  END_ROW = len(grid)-1 -1
  START_COL = 1
  END_COL = len(grid[0])-1 -1

  for i in range(START_ROW, END_ROW+1):
    for j in range(START_COL, END_COL+1):
      num_neighbors = count_neighbors_for_cell(grid, i,j)
      neighbor_grid[i][j] = num_neighbors


def create_blank_grid( grid ) -> list:
  """
  Creates a duplicate grid of the
  same size, but filled with 0s
  """
  dupe_grid = []
  for i in range(len(grid)):
    new_row = []
    dupe_grid.append( new_row )
    for j in range(len(grid[i])):
      new_row.append( 0 )
  return dupe_grid


def update_grid( grid:list, count_grid:list ):
  """
  GIVEN
  Iterate thru the count_grid using index
  and then update the grid based on the
  number of neighbors each cell has
  """
  START_ROW = 1
  END_ROW = len(grid)-1 -1
  START_COL = 1
  END_COL = len(grid[0])-1 -1

  for i in range(START_ROW, END_ROW+1):
    for j in range(START_COL, END_COL+1):
      num_neighbors = count_grid[i][j]

      # TODO: do the update rules



def init(num_rows:int, num_cols:int) -> tuple:
  """
  initialize the graphics display
  """
  pass
  global MAP_SIZE
  global SCREEN_SIZE
  global RECT_SIZE

  MAP_SIZE= { 'row' : num_rows,
              'col' : num_cols }
  SCREEN_SIZE = { 'x' : MAP_SIZE['col'] * PIXEL_SIZE,
                  'y' : MAP_SIZE['row'] * PIXEL_SIZE }
  RECT_SIZE = {'x' : SCREEN_SIZE['x'] / MAP_SIZE['col'],
                'y' : SCREEN_SIZE['y'] / MAP_SIZE['row'] }

  # initialize pygame
  pygame.init()
  screen = pygame.display.set_mode([SCREEN_SIZE['x'], SCREEN_SIZE['y']])
  pygame.display.set_caption('김 KIM-way Life')

  # only convert_alpha() if using png with transparency (alpha channel)
  # otherwise use convert()
  sprite = pygame.image.load(f'{DIR}/{SPRITE_FNAME}').convert_alpha()
  return screen, sprite


def draw_map( game_map, screen, sprite ):
  """
  draw out the map graphically using pygame.
  replaces display
  """
  for row in range( MAP_SIZE['row']):
    for col in range(MAP_SIZE['col']):
      x_start = col * RECT_SIZE['x']
      y_start = row * RECT_SIZE['y']

      # some possible background colors
      BLACK_RGB = (0,0,0)
      BLUE_RGB = (0,0,0xff)
      DODGER_BLUE_RGB = (0x1E,0x90,0xFF)

      # set the background color
      color = DODGER_BLUE_RGB

      x_len = RECT_SIZE['x'] -1
      y_len = RECT_SIZE['y'] -1

      # draw the "pixels" to the screen
      # note rect takes 4-tuple that is
      # start x,y and then width, height
      pygame.draw.rect(screen, color,
                          ( x_start, y_start,
                            x_len, y_len )
                      )

      if game_map[row][col] != 0 :
        # shift the sprite start pos a little
        # so it is centered in the pixel
        # instead of starting in the top-left corner
        # test this by setting offsets to 0,0
        sprite_start_pos = (x_start + SPRITE_OFFSET['x'],
                          y_start + SPRITE_OFFSET['y'])
        # draw the sprite to the screen
        screen.blit(sprite, sprite_start_pos)

  # refresh the display
  pygame.display.flip()


"""
start main code
"""
if __name__ == '__main__':
  SLEEP_TIME_IN_MS = 500
  DATA_FILENAME = 'conway_life_map.csv'

  # init grid and neighbors
  life_grid = read_grid_from_csv(DATA_FILENAME)
  neighbor_grid = create_blank_grid(life_grid)

  # init the graphics
  num_rows = len(life_grid)
  num_cols = len(life_grid[0])
  screen, sprite = init(num_rows, num_cols)

  # Do the first screen draw
  screen.fill( (0, 0, 0) )
  # print( life_grid )
  draw_map( life_grid, screen, sprite )

  pygame.time.wait(SLEEP_TIME_IN_MS)

  # Run until the user asks to quit
  running = True
  generation = 0
  # clock = pygame.time.Clock()

  start_time = pygame.time.get_ticks()
  while running:
    new_time = pygame.time.get_ticks()
    # print( f'{start_time} -> {new_time}')
    if ( new_time - start_time) > SLEEP_TIME_IN_MS:
      start_time = new_time
      do_counts( life_grid, neighbor_grid )
      update_grid( life_grid, neighbor_grid )
      draw_map( life_grid, screen, sprite )
      print(f'generation: {generation} ')
      generation += 1

    # get the user actions (event)
    for event in pygame.event.get():

      # Did the user click the window close button?
      if event.type == pygame.QUIT:
          running = False

      # Did the user press a key on the kb?
      if event.type == pygame.KEYDOWN:
          # did user press the 'q' key ?
        if event.key == pygame.K_q:
            print('quitting')
            running = False

          # TODO: other key actions here



    # NOTE: could also quit under different term conditions

  # Done! Time to quit.
  pygame.quit()
