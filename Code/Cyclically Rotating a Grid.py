class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])                                          #Get the dimensions.
        for i in range(min(m, n) // 2):                                         #Traverse each layer.
            layer = [grid[i][j] for j in range(i, n - 1 - i)] + \               #Put the numbers of current layer into a list, starting with the top row(except the last number).
            [grid[j][-(i + 1)] for j in range(i, m - 1 - i)] + \                #Next, the right column(except the last number).
            [grid[-(i + 1)][j] for j in reversed(range(i + 1, n - i))] + \      #Then, the bottom row(except the first number).
            [grid[j][i] for j in reversed(range(i + 1, m - i))]                 #Finally, the left column(except the first number).
            move = k % len(layer)                                               #Calculate the actual moves needed.
            layer = layer[move:] + layer[:move]                                 #Move the numbers of current layer.
            index = 0                                                           #Use index to traverse layer.
            for j in range(i, n - 1 - i):                                       #Put the numbers back to the top row(except the last number).
                grid[i][j] = layer[index]
                index += 1
            for j in range(i, m - 1 - i):                                       #Put the numbers back to the right column(except the last number).
                grid[j][-(i + 1)] = layer[index]
                index += 1
            for j in reversed(range(i + 1, n - i)):                             #Put the numbers back to the bottom row(except the first number).
                grid[-(i + 1)][j] = layer[index]
                index += 1
            for j in reversed(range(i + 1, m - i)):                             #Put the numbers back to the left column(except the first number).
                grid[j][i] = layer[index]
                index += 1
        return grid                                                             #Return grid.
