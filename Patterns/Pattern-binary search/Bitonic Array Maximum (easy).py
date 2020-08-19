"""
Bitonic Array Maximum (easy)
"""
'''
         m
      lm    mr
   l           r

 0  1  2  3   4  5   
[1, 3, 8, 12, 4, 2]
 l     m         r   
'''

    """''MEthod1''
    """
def checkpeak(arr,i):
  if i ==0:
    arr= [arr[i]-1] + arr   # add one ahead
    i +=1    
  elif i== len(arr)-1:
    arr= arr+ [arr[i]-1]   # add one ahead
  # check location

  if arr[i-1] < arr[i] and arr[i] < arr[i+1]:
    return "lm"
  elif arr[i]> arr[i+1] and arr[i] > arr[i-1]:
    return "m"
  elif arr[i-1] > arr[i] and arr[i] > arr[i+1]:
    return "mr"

def find_max_in_bitonic_array(arr):
  # TODO: Write your code here
  n = len(arr)
  l , r = 0, n -1
  i = 0
  while l <=r and i <20:
    m = (l+r)//2
    ifpeak = checkpeak(arr,m)
    if ifpeak == "m":
      return arr[m]
    elif ifpeak == "lm" :
      l = m + 1
    elif ifpeak == "mr":
      r = m - 1 
    i+=1
  return -1

'''
Method 2: Simpler:

'''

def find_max_in_bitonic_array(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    mid = start + (end - start) // 2
    if arr[mid] > arr[mid + 1]:
      end = mid
    else:
      start = mid + 1

  # at the end of the while loop, 'start == end'
  return arr[start]



def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()

