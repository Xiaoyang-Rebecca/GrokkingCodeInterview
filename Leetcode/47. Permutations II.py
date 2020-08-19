class Solution(object):
    def permuteUnique(self, nums):
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
                    if new_node not in new_ls:
                        new_ls.append(new_node ) 
                    pi+=1
            ls = new_ls
        return ls
                        