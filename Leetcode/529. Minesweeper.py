
"""#529. Minesweeper

https://leetcode.com/problems/minesweeper/
"""

''' SOlution1  DFS'''
class Solution(object):
    
    def check_range(self,i,j):
        if i >=0 and i < len(self.board) and j >=0 and j < len(self.board[0]):
            return True
        else:
            return False
    
    def check_adjacent_mines(self,i,j):
        num_of_mines= 0
        # COUNT NUMBER OF MINES
        for dir in self.dirs:
            pi,pj = i+dir[0],j+ dir[1]
            if self.check_range(pi,pj) :
                if self.board[pi][pj] == "M":
                    num_of_mines+=1
                                     
        return num_of_mines      
    
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """      
        self.board=board        
        self.dirs = [ [-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1]]
        stop_tag= False                 

        if stop_tag is False:
            if self.check_range(click[0],click[1]):
            #If a mine ('M') is revealed, then the game is over - change it to 'X'.
                if board[click[0]][click[1]]=="M":
                    board[click[0]][click[1]]="X"
                    stop_tag = True
                    return board                
                
                elif  board[click[0]][click[1]]=="E" :
                    numofmines_adj = self.check_adjacent_mines(click[0],click[1])

                    if    numofmines_adj==0 :
                        board[click[0]][click[1]]="B"
                        for dir in self.dirs:
                            pi,pj = click[0]+dir[0],click[1]+ dir[1]
                            self.updateBoard( board, [pi,pj])
                
                    else:#numofmines_adj>0 ):
                        board[click[0]][click[1]]= str(numofmines_adj)
                    
                    stop_tag= True    

        return board