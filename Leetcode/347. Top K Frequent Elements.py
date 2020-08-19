'''
347. Top K Frequent Elements
Medium

3447

222

Add to List

Share
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

'''
# Method 1: dict   Time O(n)+O(nlogn), Space:O(n)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return None
        dic = {}
        for ele in nums:
            if ele not in dic.keys():
                dic[ele] = 0
            dic[ele] +=1
        
        dic_key = sorted(dic, key=lambda i:dic[i] ,reverse=True)
        return dic_key[:k]

# MEthod 2: min heap   Time O(nlogk), Space:O(n)
import numpy as np
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        '''Get frequency''' 
        dict = {}
        for ele in nums:                        
            if ele not in dict.keys():
                dict[ele] = 0            
            dict[ele]+=1
            
        """get top K frequent """
        ls =[  ]           # frequency list, going to use min-heap
        # make sure the first on is always the smallest
        topk =[]
        print(dict)
        for ele in dict:            
            if len(ls)< k:
                # create min_heap
                ls.append(dict[ele])
                topk.append(ele)
                min_id = np.argmin(ls)
                if min_id!=0:
                    ls[0],ls[min_id] = ls[min_id],ls[0]
                    topk[0],topk[min_id] = topk[min_id],topk[0]                    
            else:
                if dict[ele]>ls[0]:                   # make sure the fist on alway the maximum
                    ls.pop(0)
                    ls.append(dict[ele])
                    topk.pop(0)
                    topk.append(ele)
                    
                    min_id = np.argmin(ls)            # minheap, make sure the first on is the smallest withinls
                    if min_id!=0:
                        ls[0],ls[min_id] = ls[min_id],ls[0]
                        topk[0],topk[min_id] = topk[min_id],topk[0]         
        return topk
