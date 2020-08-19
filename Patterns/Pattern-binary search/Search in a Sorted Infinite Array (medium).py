import math
'''
find 7
1 2 3 4 5 6 7 8 
l r                l=r+1, r*2 
    l r            l=r+1, r*2 
        l     r    binary search
'''

class ArrayReader:

  def __init__(self, arr):
    self.arr = arr

  def get(self, index):
    if index >= len(self.arr):
      return math.inf
    return self.arr[index]

def binary_search (reader,l ,r,key):
  while l <=r:
    m = (l+r)//2
    if reader.get(m) == key:
      return m
    elif reader.get(m) > key:    # move left
      r = m-1
    else:
      l = m+1
  return -1


def search_in_infinite_array(reader, key):
  # TODO: Write your code here  
  if key == reader.get(0):
    return 0
  else:
    l, r = 0, 1
    while l<=r:
      if  reader.get(l) == key:
        return l 
      if reader.get(r) == key:
        return r 

      if reader.get(l) > key:
        return  -1 
      elif reader.get(r) < key:
        l = r + 1
        r = 2* r
      else:   # *l < key < * r
        return binary_search (reader,l ,r,key)        

  return -1

def main():
  reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
  print(search_in_infinite_array(reader, 16))
  print(search_in_infinite_array(reader, 11))
  reader = ArrayReader([1, 3, 8, 10, 15])
  print(search_in_infinite_array(reader, 15))
  print(search_in_infinite_array(reader, 200))


main()







