# 1254. Number of Closed Islands
import numpy as np
'''
MNIST like
0, 4, 6, 8, 9 contains a circle
1, 2, 3, 5, 7 contains no circle

Suppose image is just 0/1 2D array
A possible 0 digit
1 1 1 1 0
1 1 0 1 1
1 1 0 0 1
0 0 1 1 1

Please write a program to detect whether there is cycle in the 2D array.
1 1 1 1 0*
1 1 0*1 1
1 1 0*0 1
0 0 1 1 1


loop all the element 
    decide if  all surrounded by 1
        if true Stoep


# set visited to 1 because 1 means surrounded

                 r
    n       s          w         e
 n s w e   n s w e  n s w e  n s w e
'''

def withinRange(p, arr):
    r =  ( p[0] >= 0 and p[1] >= 0 and p[0] <  len(arr) and p[1] < len(arr[0])  )
    return r

def atBorder(p, arr):
    r =  ( p[0] == 0 or p[1] == 0 or p[0] ==  len(arr)-1 or  p[1] == len(arr[0])-1  )
    return r

def ifsurroundedby1 (p, arr ):
    # neighbor points
    if   withinRange(p,arr) == False :                             # 1 or 0 at border
        return False 
    if  arr[p[0]][p[1]] == 1:                                     # set current point visited
        return True

    arr[p[0]][p[1]] = 1                                           # visited to 1
    r = 0
    dirs = [  [1,0], [-1,0],[0,1],[0,-1]]   
    for dir in dirs :      
        n = [ p[0] + dir[0], p[1]  + dir[1] ]
        if  ifsurroundedby1 ( n, arr ) :  # keep moving 
            r +=1
    if r == 4:
        return True
    else:
        return False


def findcycle(arr):
  for i  in range( len(arr)) :
    for j in range( len(arr[0]) ) :
        p = [i,j]
        if  arr[p[0]][p[1]] == 0 and atBorder(p, arr) == False:
            print ("p",p)

            if  ifsurroundedby1 ( p,arr ) :
                return True
  return False

arr = [[1,1,1,1,1,1,1,0],
       [1,0,0,0,0,1,1,0],
       [1,0,1,0,1,1,1,0],
       [1,0,0,0,0,1,0,1],
       [1,1,1,1,1,1,1,0]]
findcycle(arr)