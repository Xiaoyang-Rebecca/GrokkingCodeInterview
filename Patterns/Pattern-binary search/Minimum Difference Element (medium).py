import numpy as np
def search_min_diff_element(arr, key):
  # TODO: Write your code here
  diff_min = delta = np.inf
  n = len(arr) -1 
  l, r = 0, n
  while l<= r :
    m = (l+r) //2   
    diff =  arr[m] - key
    if diff == 0 :# :
      return arr[m]
    else:
      # delta = abs(diff_min - abs(diff))
      diff_min = min(diff_min, abs(diff))
      # print(diff_min,delta)      
      if diff > 0:   # move left
        r = m-1
      else:
        l = m+1
  l = min(l,n-1)
  r = max(r,0)
  return arr[l] if abs(arr[l] - key) <= abs(arr[r] - key) else arr[r]


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()
