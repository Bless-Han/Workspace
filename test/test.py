grids = [
        [ 0,11,16, 5,20],
        [17, 4,19,10,15],
        [12, 1, 8,21, 6],
        [ 3,18,23,14, 9],
        [24,13, 2, 7,22]
        ]
class Solution:
    def checkValidGrid(self, grid: list[list[int]]) -> bool:
        class Grid:
            def put_xy(self, x, y):
                self.x = x
                self.y = y
            def judge(self, grid2):
                a = grid2.x - self.x
                b = grid2.y - self.y
                return abs(abs(grid2.x - self.x) - abs(grid2.y - self.y)) == 1
                return False


        tour = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                tour.append(Grid())

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                tour[grid[i][j]].put_xy(i, j)

        for t in tour:
            print(t.x, t.y)

        for i in range(len(tour)-1):
            if tour[i].judge(tour[i+1]) == False:
                print("-" * 20)
                print(tour[i].x, tour[i].y)
                print(tour[i+1].x, tour[i+1].y)
                return False
                



        return True

s = Solution()
print(s.checkValidGrid(grids))
