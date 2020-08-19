class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def checksingle(nums,i):
            ifsingle = False
            nextdir = None
            if i ==0:
                if len (nums) == 1:
                    ifsingle = True
                else:
                    if nums[i+1] !=  nums[i]:
                        ifsingle = True
                    else:
                        ifsingle, nextdir =  False,"r"   # shoule move right
            elif i == len(nums) -1:
                if nums[i] != nums[i-1]:
                    ifsingle = True
                else:
                    ifsinge =  False, "l"      # should mover left
            else: # *1 --- *n-2
                if nums[i]!= nums[i-1] and nums[i]!= nums[i+1]:
                    ifsingle = True
                else:
                    if (nums[i] == nums[i+1] and i%2==0) or  (nums[i] == nums[i-1] and i%2==1):
                        nextdir = "r"
                    else:
                        nextdir = "l"
            return ifsingle,nextdir
        
        n = len(nums) -1
        l ,r = 0, n
        ifsingle = False
        # i = 0
        while l<=r and ifsingle == False :
            m = (l+r) //2
            ifsingle,nextdir = checksingle(nums,m)
            # print(l,r,m,ifsingle, nextdir)
            if ifsingle :
                return nums[m]
            else:
                if nextdir == "l":
                    r = m-1
                else:
                    l = m+1
            # i +=1
        return -1
                    
        