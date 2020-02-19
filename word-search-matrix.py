class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def getCells(seen, i, j):
            for nr, nc in ((i+1, j), (i-1,j), (i, j+1), (i, j-1)):
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and not seen[nr][nc]:
                    yield nr, nc
            
            
        def bfs(seen, i, j, cur):
            # print("start",i, j, board[i][j], cur)
            if cur == len(word) and word[cur-1] == board[i][j]:
                return True

            for nr, nc in getCells(seen, i, j):
                if board[nr][nc] != word[cur]:
                    continue
                seen[nr][nc] = True
                if bfs(seen, nr,nc, cur + 1):
                    return True
                seen[nr][nc] = False

            return False
            
            #walk right 
            #walk left
            #walk up
            #walk down
            
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    seen = [[False for j in range(len(board[0]))] for i in range(len(board))]
                    seen[i][j] = True
                    # print(i, j, board[i][j])
                    if bfs(seen, i, j, 1):
                        return True
        return False

sol = Solution()
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABFSADECCESC"))

for i in [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]:
    print(i)