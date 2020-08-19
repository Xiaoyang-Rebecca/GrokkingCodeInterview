'''
O(N∗2^​N​​ ).
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        result = []
        ls = [ {"s":"","left":0,"right":0} ]      # info = "", openCount,closeCount
        while len(ls) > 0:
            p = ls.pop(0)
            if p["left"] == n and p["right"] == n:
                result.append(p["s"])
            else:
                if p["left"] > p["right"]:
                    ls.append({ "s":p["s"] + ")" , "left": p["left"], "right":p["right"]+1   })
                    
                if p["left"] < n:           
                    ls.append({ "s":p["s"] + "(" , "left": p["left"]+1, "right":p["right"]   })

        return result
                    


def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))
