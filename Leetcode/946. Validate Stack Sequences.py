
'''
Method 1
Time 0(n)
'''
class Solution(object):
    def validateStackSequences(self, p1, p2):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
                                  action
         [1,2,3,4,5] [4,3,5,1,2]
          i           j            push(1)
            i         j            push(2)
              i       j            push(3)
                i     j            push(4)       i =j
                i       j          pop(4)
                i     j            push(5)       i =j
                  i       j        pop(5)        i=n
                  
        """
        stack = []
        i,j = 0,0
        n = len(p1)
        while i < n and j < n:
            while i < n and p1[i] != p2[j]:
                stack.append(p1[i])
                i += 1
            j += 1; i += 1
            while j < n and stack and p2[j] == stack[-1]:
                stack.pop()
                j += 1

        return len(ls) ==0


'''
Method 2
Time 0(n)
'''
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)
                