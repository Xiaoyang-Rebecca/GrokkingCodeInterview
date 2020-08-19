
"""1041. Robot Bounded In Circle (Medium)
Favorite

Share
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
"""

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
    
    
        x = 0
        y = 0
        d = "N"

        d_l_loop = ["N","W","S","E","N"]
        d_r_loop = d_l_loop[::-1]
        print (d_r_loop)
        for i in instructions:
            if i == "G":
                if d == "N":
                    y +=1
                elif d == "S":
                    y -=1
                elif d == "W":
                    x -= 1
                else:
                    x +=1
            elif i == "L":
                d = d_l_loop[d_l_loop.index(d)+1]
            else:
                d = d_r_loop[d_r_loop.index(d)+1]
            print (i,"(" , x,",",y,")", "next d:",d)

        if d !="N" or (x==0 and y==0):
            return True
        else:
            return False

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        res = []
        q =collections.deque() # storage the id
        for i in range (len(nums)):
            if len(q)>0 and q[0] == i-k:
                q.pop()
            print (q)
            while len(q)>0  and nums[q[-1]] < nums[i]:
                q.popleft()
                
            q.append(i)
            print (i,q)
            if i>=k -1:
                res.append (nums[q[0]])
        return res
