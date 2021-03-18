class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up, down, result = 1, 1, 1            #Store the length of upward wiggle subsequence ending at previous number, the length of downward wiggle subsequence ending at previous number and max length of wiggle subsequence.
        for i in range(1, len(nums)):         #Traverse from 2nd number.
            if nums[i] > nums[i - 1]:         #If current number is larger than previous number, new length of downward wiggle subsequence ending at current number equals the length of upward wiggle subsequence ending at previous number plus 1.
                up = down + 1
                result = max(result, up)      #Update max length of wiggle subsequence.
            elif nums[i] < nums[i - 1]:       #If current number is smaller than previous number, new length of upward wiggle subsequence ending at current number equals the length of downward wiggle subsequence ending at previous number plus 1.
                down = up + 1
                result = max(result, down)    #Update max length of wiggle subsequence.
        return result                         #Return max length of wiggle subsequence.
