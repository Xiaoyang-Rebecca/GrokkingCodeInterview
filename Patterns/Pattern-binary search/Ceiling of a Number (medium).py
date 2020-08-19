import numpy as np
def search_ceiling_of_a_number(arr, key):
  # TODO: Write your code here
  l , r = 0, len (arr) -1     # ascending order, arr[l] <= arr[r]
  diff_min = arr[r] - key    # ele - key >=0
  i = r
  if diff_min < 0:
    return -1  
  if arr[l] > key:
    return 0
  while r < len(arr) :#and c < 20 and delta >0:
    # delta = m - 
    m = int( ( l + r)/2 )
    diff = arr[m] - key

    if diff > 0:     
      r = m -1                    # move to left      
      if diff < diff_min:
        diff_min = diff
        i = m   
      elif diff == diff_min:
        return i
    elif diff < 0:
      l = m +1
    else:
      return m



def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
