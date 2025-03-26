class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])                                            #Get the dimensions.
        nums = sorted(grid[i][j] for i, j in product(range(m), range(n)))         #Sort numbers in grid.
        if any((nums[i + 1] - nums[i]) % x for i in range(len(nums) - 1)):        #If the difference between any 2 adjacent numbers could not be divide by x, return -1 because they can neven be equal after any number of operations.
            return -1
        total = sum((y - nums[0]) // x for y in nums[1:])                         #Calculate the total number of operations to change all numbers to nums[0]
        result = total                                                            #Initialize result to be total.
        for i in range(1, len(nums)):                                             #Traverse the rest of nums.
            total -= (len(nums) - 2 * i) * (nums[i] - nums[i - 1]) // x           #Update the number of operations to move all numbers to nums[i]; basically for nums[i:], they decrease (nums[i] - nums[i - 1]) // x operations while for nums[:i], they increase (nums[i] - nums[i - 1]) // x operations.
            result = min(result, total)                                           #Update result if necessary.
        return result
