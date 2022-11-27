class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        subsequences = [defaultdict(int) for _ in range(len(nums))]         #Store the count of arithmetic subsequences ending at current index by common difference.
        count = 0
        for i in range(len(nums)):                                          #Traverse nums.
            for j in range(i):                                              #Traverse nums[i].
                diff = nums[i] - nums[j]                                    #Get the diff(nums[i] - nums[j])
                count += subsequences[j][diff]                              #Increase count with subsequences[j][diff], because there will be subsequences[j][diff] new aruthmetic slices ending at nums[j] extending to nums[i].
                subsequences[i][diff] += subsequences[j][diff] + 1          #subsequences[j][diff] + 1 to subsequences[i][diff], because [nums[j], nums[i]] makes a subsequence as well.
        return count                                                        #Return count.
