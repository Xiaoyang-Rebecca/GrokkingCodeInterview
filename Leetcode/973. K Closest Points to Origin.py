'''
Method 1 , O(n)

'''
class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]

'''
Method 2 , Maxheap O(n)
'''
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """ 

        pq = []
        for x1,y1 in points:
            distance = ((x1**2) + (y1**2)) ** 0.5
            heappush(pq,(-distance,(x1,y1)))
            if len(pq) > k:
                heappop(pq)
        res = []
        while pq:
            axis = heappop(pq)[1]
            res.append([axis[0],axis[1]])
        return res

'''
Maxmimum:
  # first one always the max
  for i, ele in point:
      if i < K:
          ls.append(dist)
      else:
          if dist < ls []:
              ls[0] = ele

      ls = maxheap(s)
'''

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """ 
        import numpy as np
        def maxheap(ls):                         # Time O(n)
            #ls = [ [dist,ele]]                  # the order is dist
            max_id = np.argmax( [ i[0] for i in ls])
            # print("ls=",ls, "max_id=",max_id)
            if max_id!=0:
                ls[0], ls [max_id] = ls[max_id], ls [0]
            return ls
        
        ls = []    # max heap
        for i, ele in enumerate( points) :
            if i < K:
                ls.append([dist,ele])                
                ls = maxheap(ls)    
            else:
                dist = (ele[0] **2 + ele[1]**2) 

                if dist < ls[0][0]:
                    ls[0] = [dist,ele]
                    ls = maxheap(ls)     
        return [ i[1] for i in ls]