class Solution:
    def pathSum(self, nums: List[int]) -> int:
        levels = [[-1], [-1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1]]                        #Use arrays to simulate the 4 levels of binary tree.
        for x in nums:                                                                                       #Traverse nums to populate the value at each position.
            levels[x // 100 - 1][(x % 100) // 10 - 1] = x % 10
        result = 0
        for i in range(4):                                                                                   #Traverse all levels.
            for j in range(len(levels[i])):                                                                  #Traverse current level.
                if levels[i][j] == -1:                                                                       #If current value is -1, there is no node here, skip.
                    continue
                if i + 1 < 4 and levels[i + 1][2 * j] != -1:                                                 #If current node has left child, plus current value to the value of its left child.
                    levels[i + 1][2 * j] += levels[i][j]
                if i + 1 < 4 and levels[i + 1][2 * j + 1] != -1:                                             #If current node has right child, plus current value to the value of its right child.
                    levels[i + 1][2 * j + 1] += levels[i][j]
                if i + 1 == 4 or (levels[i + 1][2 * j] == -1 and levels[i + 1][2 * j + 1] == -1):            #If current node is leaf node, add its value to result.
                    result += levels[i][j]
        return result
