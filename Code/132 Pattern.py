class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, minValue = [], [nums[0]]                                    #Initialize mono decreasing stack to store numbers visited backwards and initialize min value at in nums[:i + 1], 0 <= i < len(nums).
        for x in nums[1:]:                                                 #Populate nums.
            minValue.append(min(minValue[-1], x))
        for j in reversed(range(len(nums))):                               #Traverse nums backwards.
            if nums[j] > minValue[j]:                                      #If nums[j] > minValue[j], we need to find if there is a number in nums[j + 1:] that is greater than minValue[j]. For the nums[j] <= minValue[j], it will be also smaller than any minValue[k] 0 <= k < j, as minValue[k] >= minValue[j].
                while stack and stack[-1] <= minValue[j]:                  #While stack id not empty and top of stack is smaller than or equal to minValue[j], pop stack.
                    stack.pop()
                if stack and stack[-1] < nums[j]:                          #If stack is not empty and top of stack is smaller than nums[j], since stack is mono decreasing so the top of stack is smallest, we found a 132 triplet, return true.
                    return True
                stack.append(nums[j])                                      #Append nums[j] to stack; since stack[-1] >= nums[j], stack is still mono decreasing.
        return False                                                       #Return false if cannot found.
