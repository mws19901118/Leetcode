class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if len(A) == 0 or len(A[0]) == 0:       #Handle empty list.
            return 0
        curr = A[-1]                            #Use curr to store the min falling path sum for each element in current level as the starting number. We do dp bottum up, so initially it's the lowest level in A.
        for i in reversed(range(len(A) - 1)):   #Do DP bottom up.
            upper = []                          #Store the min falling path sum for each element in upper level as the starting number.
            for j, x in enumerate(A[i]):        #Traverse through upper level.
                t = curr[j]                     #The min falling path sum for index j is A[i][j] + min(curr[j - 1], curr[j], curr[j + 1]) if j - 1 and j + 1 are valid index.
                if j > 0:
                    t = min(t, curr[j - 1])
                if j < len(A[i]) - 1:
                    t = min(t, curr[j + 1])
                upper.append(t + x)             #Append min falling path sum for index j to upper.
            curr = upper                        #Replace curr with upper as we finished DP on current level.
        return min(curr)                        #Return the min value of curr, which is the min falling path sum of top level after DP.
