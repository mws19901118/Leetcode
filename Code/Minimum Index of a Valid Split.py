class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)                                                                                #Count each number.
        max_count = max(count.values())                                                                      #Find the max count.
        dominate_number = [x for x in count if count[x] == max_count][0]                                     #Find the dominate number.
        current_count = 0                                                                                    #Initialize current count of dominate number.
        for i, x in enumerate(nums):                                                                         #Traverse nums.
            current_count += x == dominate_number                                                            #Update current count.
            if current_count > (i + 1) // 2 and (max_count - current_count) > (len(nums) - 1 - i) // 2:      #If the dominate number dominates both nums[:i + 1] and nums[i + 1:], we can split here so return i.
                return i
        return -1                                                                                            #Return -1 if cannot find a valid split.
