def binary_search(arr, key):
  # TODO: Write your code here
  # sorted array, l,m,r
  l , r = 0,len(arr)-1
  while r < len(arr):
    m = int(  (l+r)/2 )
    if arr[l] == key:
      return l
    if arr[r] == key:
      return r 
    if arr[m] ==key:
      return m 

    if arr[l] <= arr[m]:   # increading order
      l = m
    else:
      r = m 
  
  return m

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()
