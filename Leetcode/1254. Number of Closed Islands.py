@@ -1,78 +0,0 @@
# 1254. Number of Closed Islands
import numpy as np
'''
Suppose image is just 0/1 2D array
A possible 0 digit
1 1 1 1 0
1 1 0 1 1
1 1 0 0 1
0 0 1 1 1

loop all the element 
    decide if  all surrounded by 1
        if true Stoep


'''

def withinRange(p, arr):
    r =  ( p[0] >= 0 and p[1] >= 0 and p[0] <  len(arr) and p[1] < len(arr[0])  )
    return r

def atBorder(p, arr):
    r =  ( p[0] == 0 or p[1] == 0 or p[0] ==  len(arr)-1 or  p[1] == len(arr[0])-1  )
    return r

'''
Method 1 : BFS  Time:0(n*n), Space o (n)
'''
def ifsurroundedby1 (p, arr):                               # # inital 0 point or adjacent 0 neighbors
                                                             
    arr[p[0]][p[1]] = 1                                      # set current point visited to 1
    dirs = [  [0,-1], [-1,0],[0,1],[1,0]]                    # clock wise
    ls = [p]                                                 # the loc id of remaining 0s
    numOfNeighbor1 = 0
    hitborder = False
    while len(ls) > 0:
        p = ls.pop(0)
        numOfNeighbor1 = 0
        for dir in dirs :      
            n = [ p[0] + dir[0], p[1]  + dir[1] ]
            if withinRange(n,arr) == False :                  # outside range 
                pass
            else:
                if arr[n[0]][n[1]] == 1 :                        
                    numOfNeighbor1 += 1
                else: #arr[n[0]][n[1]] == 0                  # neighbor cell is zero
                    if atBorder(n, arr) ==True:              # neighbor 0 at edge, not a close island
                        hitborder = True                         # need to keep updating 
                    arr[n[0]][n[1]] =  1                     # flip it to visited
                    ls.append(n)
        # print ("ls=",ls,"neighbors=",numOfNeighbor1  )
        
    if numOfNeighbor1 == 4 and hitborder== False:                                  # True only when the last 0 is all surrouded by 1
        return True
    else:
        return False

'''
Method 2 : DFS  Time: 0(n*n), Space o (1)       
                r
    n       s          w         e
 n s w e   n s w e  n s w e  n s w e
'''
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


def main(arr):
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
main(arr)


'''
Extension: plot cube
'''

def cube_show_slider(cube, axis=2, **kwargs):
    """
    Display a 3d ndarray with a slider to move along the third dimension.

    Extra keyword arguments are passed to imshow
    """


    # check dim
    if not cube.ndim == 3:
        raise ValueError("cube should be an ndarray with ndim == 3")

    # generate figure
    fig = plt.figure()
    
    ax = plt.subplot(111)
    fig.subplots_adjust(left=0.25, bottom=0.25)
    
    # select first image
    s = [slice(0, 1) if i == axis else slice(None) for i in range(3)]
    im = cube[s].squeeze()
    ax.set_title( "axis="+ str(s[-1]) )

    # display image
    l = ax.imshow(im, **kwargs)

    # define slider
    ax = fig.add_axes([0.25, 0.1, 0.65, 0.03])

    slider = Slider(ax, 'Axis %i index' % axis, 0, cube.shape[axis] - 1,
                    valinit=0, valfmt='%i')

    def update(val):
        ind = int(slider.val)
        s = [slice(ind, ind + 1) if i == axis else slice(None)
                 for i in range(3)]
        im = cube[s].squeeze()
        l.set_data(im, **kwargs)
        fig.canvas.draw()

    slider.on_changed(update)
    
    plt.show()
    