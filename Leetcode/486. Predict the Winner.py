
"""#486. Predict the Winner

Share
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
"""

'''
   [1, 5, 23, 7]              winA         win B 
    a              [5,23,7]   
       b           [23,7]                 5 -23 = -18
           a       [5]        23 - 5=18
              b    [23]                   7-23 = 


'''
 
def getscore(arr, first, end):
    if first == end:
        return arr[first]
    else:
        # how much score it earn 
        return max( arr[first] - getscore(arr, first + 1, end)  ,
                    arr[end]   - getscore(arr, first , end-1) )     
def ifwin(arr):
    return getscore(arr,0,len(arr)-1) >=0
ifwin( [1, 5, 233, 7])
