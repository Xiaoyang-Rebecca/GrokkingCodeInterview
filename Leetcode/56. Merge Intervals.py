"""56. Merge Intervals

https://leetcode.com/problems/merge-intervals/
"""

#@title

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """      
        self.interval_len = len(intervals)      
        interval_deltas = 1
        while interval_deltas != 0 :
            new_merged = self.merge_intervals(intervals)            
            interval_deltas = self.interval_len- len(new_merged)
            intervals = new_merged        
            self.interval_len = len(intervals) 
            
        result = intervals
        return result

    def merge_interval_pair (self,i,j):
        if min(i) > min(j):  # make sure i is the smaller one
            i, j = j , i
        # merge
        if max(i) < min(j) :
            return  [i,j]
        else:
            return [[ min( min(i),min(j)),max(max(j),max(i))]]

    def merge_intervals (self,intervals):        
        # print ("intervals=",intervals)
        its = intervals
        if len(its) <=1:
            r = its            
        else:    
            r = []
            pi = 0
            it_ids = [i for i in range(len(intervals))]            
            while pi in it_ids:                
                i = its[pi]                             # pointer pi for interval i 
                pj = pi+1
                while pj in it_ids and pi in it_ids:    # pointer pj for interval j , pi might be deleted
                    j = its[pj]      
                    checked_its = self.merge_interval_pair (i,j)  
                    if len(checked_its) == 1:
                        it_ids.remove(pi)
                        it_ids.remove(pj)    
                        its.remove(i)
                        its.remove(j)
                        its.append(checked_its[0])      # add new intervales 
                        # print ("its=",its)
                        # break
                    pj+=1
                pi+=1
                
                r +=checked_its 

        # print ("r=",its)
        return its

s = Solution()
s.merge([[1,3],[2,16],[8,10],[15,18]])    # [[1,18]]