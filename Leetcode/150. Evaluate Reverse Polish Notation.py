class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
 
        for token in tokens:
            if token in ('+-*/'):
                b = stack.pop()
                a = stack.pop()
                if token == '+':   stack.append(a+b)
                elif token == '-': stack.append(a-b)
                elif token == '*': stack.append(a*b)
                else:
                    c = a//b      
                    if c<0: 
                        stack.append(-1*(-a//b))
                    else:
                        stack.append(c)
                print(stack)
            else:
                stack.append(int(token))
        return stack.pop()            
 
 
                