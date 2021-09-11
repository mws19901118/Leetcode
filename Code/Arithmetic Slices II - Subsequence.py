class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        subsequences = [defaultdict(int) for _ in range(len(nums))]         #Store the count of arithmetic subsequences ending at current index by common difference.
        pairs = [defaultdict(int) for _ in range(len(nums))]                #Store the count of number pairs ending at current index by difference.
        count = 0
        for i in range(len(nums)):                                          #Traverse nums.
            for j in range(i):                                              #Traverse nums[i].
                diff = nums[i] - nums[j]                                    #Get the diff(nums[i] - nums[j])
                if diff in subsequences[j]:                                 #If diff is in subsequences[j], so all arithmetic subsequences ending at j with common difference diff can extend to i.
                    subsequences[i][diff] += subsequences[j][diff]
                if diff in pairs[j]:                                        #If diff in pairs[j], so all number pairs ending at j whose difference is diff can form an arithmetic subsequence with nums[i]. 
                    subsequences[i][diff] += pairs[j][diff]
                pairs[i][diff] += 1                                         #Add the pair (nums[j], nums[i]) to pairs[i] by diff.
            count += sum(subsequences[i].values())                          #Add total values for subsequences[i] to count.
        return count                                                        #Return count.
