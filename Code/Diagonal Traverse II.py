class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)                    #Store each diagonal in reverse order.
        for i, row in enumerate(nums):                   #Traverse each row.
            for j, x in enumerate(row):                  #Traverse each element in current row.
                diagonals[i + j].append(x)               #Append x to its diagonal.
        result = []                                      #Initialize result to be an empty array.
        for i in range(max(diagonals.keys()) + 1):       #Traverse from first diagonal to last diagonal.
            result.extend(diagonals[i][::-1])            #Extend the reversed diagonal to result.
        return result
