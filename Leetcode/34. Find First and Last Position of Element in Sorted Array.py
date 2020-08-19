''' method 1
Time 0(n) , Space (1)
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rg = []
        for i,ele in enumerate(nums):
            if ele == target :
                if len(rg) <2 :
                    rg.append(i)
                else:  #len ==2
                    rg[1] = i
        if len(rg) == 0:
            return [-1,-1]
        elif len(rg) == 1:
            return [rg[0],rg[0]]
        else:
            return rg
                    
            
''' method 2
3 binary search  O(3* log(n))
'''
class Solution(object): 
   
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l ,r = 0, len(nums)-1
        temp = None
        while l <= r  :
            m = (l + r) //2 
            if  nums[m] == target :  # find target
                temp =m     
                break
            if nums[m] > target: # move to left
                r = m-1
            else:
                l = m+1
                
        if temp != None:
            mini ,maxi = temp, temp            
            # look for i min to target
            if mini > 0:
                l ,r = 0, temp                
                while l <= r:
                    m =  (l + r) //2
                    if l==0 and nums[l] == target:                  # mini is 0, directly output
                        mini = 0
                        break                    
                                                                    # else keep loop
                    if nums[m] == target and nums[m-1] < target  :
                        mini = m
                        break
                    elif nums[m] < target:
                        l = m+1           # move right
                    else:
                        r = m-1
                                    
            # look for i max to target
            if maxi < len(nums ) -1:
                l ,r = temp, len(nums ) -1
                while l <= r :
                    m = (l + r) //2
                    if nums[m] == target and m == len(nums ) -1:   # mini is n-1, directly output
                        maxi = m
                        break                        
                    if nums[m] == target and nums[m+1] > target :  # else keep loop
                        maxi = m
                        break
                    elif nums[m] > target:
                        r= m-1          # move right
                    else:
                        l = m+1                            
            return [mini ,maxi]
        else:
            return [-1,-1]
                

                    
            


return [-1,-1] if nums.count(target) == 0 else [nums.index(target), len(nums)-1-nums[::-1].index(target)]