'''
   maxheap  minheap
   ele      None
   <min     None
'''
import heapq 
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # initalize
        if len(self.maxheap) ==0 or num <= -self.maxheap[0] :
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        
        # adjust balance
        if len(self.maxheap) > len(self.minheap)+1:
            ele = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, ele)
        elif len(self.minheap) > len(self.maxheap): 
            ele = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -ele)            
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minheap)==0 and len(self.maxheap)==0:
            return None


        if len(self.minheap) == len(self.maxheap) :
            return (float(self.minheap[0]) - float(self.maxheap[0] ) )/2.0
        else:
            return -self.maxheap[0] * 1.0


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()