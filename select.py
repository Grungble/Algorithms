"""
SELECTION SORT
(suboptimal)
algorithm:
  - go thru the unsorted list
  - find the max value and take out of unsorted list
  - put the max value into the new sorted list
  - keep going thru the unsorted list
"""

def extract_max_value( my_list: list ) :
  """
  find the max in the list and then
  remove it from the list 
  return the value
  """
  max_index = 0
  max_value = my_list[ max_index ]
  for index, value in enumerate(my_list):
    if value > max_value:
      max_index = index
      max_value = value
  
  my_list.pop( max_index )
  return max_value



if __name__=='__main__':
  DO_ASCENDING = False

  unsorted_list = [ 6, 9, 3, 1, 7, 22, 11 ]
  sorted_list   = [ ]
  
  while len( unsorted_list ) > 0:
    unsorted_max = extract_max_value( unsorted_list )

    # put at the beginning or end depending
    # on which way we want to sort
    if DO_ASCENDING:
      sorted_list.insert(0, unsorted_max )
    else:
      # sorted_list.append( unsorted_max )
      n = len(unsorted_list)
      sorted_list.insert(n, unsorted_max )

    # ALT (ternary operator)
    # insertion_point = 0 if DO_ASCENDING else len(unsorted_list)
    # sorted_list.insert( insertion_point, unsorted_max )

  print( sorted_list )