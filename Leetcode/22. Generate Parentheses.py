'''
22. Generate Parentheses
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        ls = ["("]
        for i in range (2*n-1):
            new_nodes = []
            for node in ls:
                numOfLeft=0
                for p in node:
                    if p == "(":
                        numOfLeft+=1 
                numOfRight = len(node) - numOfLeft                
                # print ("Node"+node+",Right="+str(numOfRight)+",left="+str(numOfLeft))
                # add ")"
                if numOfLeft > numOfRight and numOfLeft <= n:
                    new_node = node + ")"  
                    new_nodes.append(new_node)                    
                # add "("
                if numOfRight <= n and numOfLeft < n:
                    new_node = node + "("  
                    new_nodes.append(new_node)   
            ls = new_nodes
        return ls
                    
