import numpy as np


# Method1, use a min_ls to storage the current min value
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ls = []
        self.min_ls = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.ls.append(x)
        if len(self.min_ls) == 0:
            self.min_ls .append( x ) 
        else:
            current_min = min(self.min_ls[-1], x)
            self.min_ls. append (current_min)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.ls) > 0:
            self.ls.pop()
            self.min_ls.pop()                  

    def top(self):
        """
        :rtype: int
        """
        return self.ls[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_ls[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()