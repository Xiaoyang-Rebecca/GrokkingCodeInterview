
"""#346. Moving Average from Data Stream

Share
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.maxSize = size  # actual number of ele
        self.eles = []
        self.sum = 0.0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """        
          
        self.eles.append(val)                
        if len (self.eles) > self.maxSize: 
            self.sum  =  self.sum -self.eles[0]
            self.eles.remove(self.eles[0])   
            
        self.sum = self.sum  + val
        
        return self.sum/len (self.eles)
