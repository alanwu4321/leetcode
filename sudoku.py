class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def possible(x,y,n):
            for i in range(0,9):
                if board[i][y] == n:
                    return False
            for j in range(0,9):
                if board[j][i] == n:
                    return False
            sx = (x // 3) * 3
            sy = (y // 3) * 3
            for i in range(0,2):
                for j in range(0,2):
                    if board[sx + i][sy + j] == n:
                        return False
            return True
                    
        def findEmpty():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == -1:
                        return i,j
            return -1,-1
        
        def solve(board):
            i, j = findEmpty()
            print(i,j)
            if i == -1:
                return True
            for num in range(0,10):
                if possible(i,j, num):
                    board[i][j] = num
                    if solve(board):
                        return True
                    board[i][j] = -1
            return False


        for ind, i in enumerate(board):
            for indj, j in enumerate(i):
                if j != ".":
                    board[ind][indj] = int(board[ind][indj])
                else:
                    board[ind][indj] = -1

        solve(board)
       
        return board
                    

input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sol = Solution()
print(sol.solveSudoku(input))


def findNextCellToFill(grid, i, j):
        for x in range(i,9):
                for y in range(j,9):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1

def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def solveSudoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValid(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False

# print solveSudoku(input)