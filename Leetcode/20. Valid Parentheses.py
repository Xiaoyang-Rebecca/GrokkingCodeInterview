
"""#20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/solution/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valids


    example: 
       {  [   ( ) ] }
"""

def demo (str):
    """
    :type s: str
    :rtype: bool
    
    "( ) [ ] { }"  stack
        i             (
        i           ()
    
    """
    
    dic = { ")": "(" , "]":"[", "}":"{"}
    stack = []
    for ele in str:
        if ele in dic.values():   # left
            stack.append (ele)
        elif ele in dic.keys():  # right 
            if len(stack)==0:
                return False
            else:
                if dic[ele] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
    return len(stack) ==0

demo(  " {  [   ( ) ]} "    )