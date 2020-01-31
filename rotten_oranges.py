#rotten oranges

test = [[2,1,1],[1,1,0],[0,1,1]]

class Orange:
    def __init__(self, row, col, layer):
        self.row = row
        self.col = col
        self.layer = layer

class Rot:
    def rot(self,grid):
        Xdir = [0,0,1,-1]
        Ydir = [1,-1,0,0]
        maxLayer = 0
        R = len(grid)
        C = len(grid[0])
        que = list()

        #populate queue with all bad oranges
        for r, row in enumerate(grid):
            for c, orange in enumerate(row):
                if orange == 2:
                    que.append(Orange(r,c,0))
        # '''
        # option1
        # '''
        # def inside(r, c):
        #     if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        #         return False
        #     return True
        
        # #start rottening up, down, left and right orange
        # #update the layer
        # #while que
        # layer = 0 
        # while que:
        #     #get the first orange
        #     org = que.pop(0)
        #     print(org.layer)
        #     #check all four direction for healthy orange
        #     for i, val in enumerate(Xdir):
        #         x = org.row - val
        #         y = org.col - Ydir[i]
        #         layer = org.layer
        #         #rot if the adjacent one is healthy
        #         if inside(x, y) and grid[x][y] == 1:
        #             grid[x][y] = 2
        #             newLayer = org.layer+1
        #             que.append(Orange(x,y,newLayer))
        #             # maxLayer = max(maxLayer,newLayer)

        '''
        option2
        create a generator to check 4 directions
        to replcae >>>
           for i, val in enumerate(Xdir):
                x = org.row - val
                y = org.col - Ydir[i]
        '''

        def getDir(org):
            r = org.row
            c = org.col
            #generator
            for nr,nc in ((r + 1, c), (r - 1, c),(r, c + 1),(r, c - 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr,nc


        layer = 0 
        while que:
            #get the first orange
            org = que.pop(0)
            print(org.layer)
            #check all four direction for healthy orange
            layer = org.layer
            for nr, nc in getDir(org):
                #rot if the adjacent one is healthy
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    que.append(Orange(nr,nc,layer+1))
                    # maxLayer = max(maxLayer,newLayer)

        if any(1 in row for row in grid):
            return -1
        
        return layer


a = Rot()
print(a.rot(test))

# def test_rot():
#     a = Rot()
#     # print(a.rot(test))
#     assert a.rot(test) == 4

