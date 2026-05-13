class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        diff = [0] * (2 * limit + 2)                                                  #The target sum is from 2 to 2 * limit, suppose the target sum is x, so use a diff array of (2 * limit + 2) to store the diff of moves from x - 1 to x.
        for i in range(len(nums) // 2):                                               #Traverse each pair in nums.
            a, b = min(nums[i], nums[-(i + 1)]), max(nums[i], nums[-(i + 1)])         #Get the smaller and larger value between nums[i] and nums[-(i + 1)].
            diff[2] += 2                                                              #If 2 <= x < a + 1, we need to replace both a and b, so increase diff[2] by 2.
            diff[a + 1] -= 1                                                          #If a + 1 <= x < a + b, we only need to replace b to x - a, so decrease diff[a + 1] by 1.
            diff[a + b] -= 1                                                          #If x == a + b, no move needed, so decrease diff[a + b] by 1.
            diff[a + b + 1] += 1                                                      #If a + b <= x < b + limit + 1, we only need to replace a to x - b, so increase diff[a + b + 1] by 1.
            diff[b + limit + 1] += 1                                                  #If b + limit + 1 <= x, we need to replace both a and b, so increase diff[b + limit + 1] by 1.

        result, curr = len(nums), 0                                                   #Initialize result and current.
        for x in range(2, 2 * limit + 1):                                             #Traverse from 2 to 2 * limit.
            curr += diff[x]                                                           #Add diff[x] to curr.
            result = min(curr, result)                                                #Update result if necessary.
        return result
