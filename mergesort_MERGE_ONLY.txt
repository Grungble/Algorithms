"""
mergesort
Merge code only
"""
def merge_sorteds(left_arr:list, right_arr:list ) -> list:
  """
  merge the 2 sorted lists
  PRECONDITION: the left list and right list are both pre-sorted
  POSTCONDITION: the original lists are unchanged
  """
  new_arr = [ ]

  return new_arr


def merge_sorteds_BAD(left_arr:list, right_arr:list ) -> list:
  """
  DO NOT DO THIS
  merge the 2 sorted lists
  PRECONDITION: the left list and right list are both pre-sorted
  POSTCONDITION: the original lists are unchanged
  """
  new_arr = left_arr + right_arr
  new_arr.sort()
  return new_arr


if __name__=='__main__':
  my_left_list = [ 1, 10, 20, 30, 40]
  my_right_list = [ 2,3,4,5,6, 11, 49]

  merged_list = merge_sorteds_BAD( my_left_list, my_right_list )
  expected_list = [1, 2, 3, 4, 5, 6, 10, 11, 20, 30, 40, 49]
  print( merged_list )
  # NOTE: this actually works (why is that "interesting"?)
  assert( merged_list == expected_list )