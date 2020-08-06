
"""# 281. Zigzag Iterator"""

'''Method1: list (storage consumming)'''
class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        
        r = []
        for l in range(max(len(v1),len(v2))):
            if l < len(v1):
                r.append(v1[l])
            if l < len(v2):
                r.append(v2[l])
        self.r = r
        self.id = 0
    def next(self):
        """
        :rtype: int
        """        
        r = self.r[self.id] 
        self.id+=1
        return    r       

    def hasNext(self):
        """
        :rtype: bool
        """       
        return  self.id < len(self.r)
        
v1,v2=[1,2],[3,4,5,6]
i, v = ZigzagIterator(v1, v2), []
i.hasNext()
while i.hasNext():
    
    v.append(i.next()):