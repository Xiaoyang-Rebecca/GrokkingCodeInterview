'''
e.g.              [1,2,3,4]
1                      [1]
2                  [2,1] [1,2]
3  [3,2,1][3,1,2] [2,3,1][1,3,2][2,1,3][1,2,3]    # 3*2*1
 
 Space:0(n!)
 Time: O(n!)
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0 :
            return None
        ls =[ [nums[0]] ]                                    # header
        for i, ele in enumerate(nums[1:]):
            new_ls = []          
            for node in ls:                                   # len(node) = i+1
                pi = 0
                while pi <=len(node):                         # positions 0 .. i
                    new_node = node[:pi] + [ele] +node[pi:]
                    new_ls.append(new_node ) 
                    pi+=1
            ls = new_ls
        return ls
                