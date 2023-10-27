class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = [-1] * len(nums)                                                                                        #For each number, store the first index to the left that is smaller than current number; initially it's -1 means no smaller number to the left.
        stack = []                                                                                                     #Use a stack to store indexes whose numbers are in increasing order.
        for i in reversed(range(len(nums))):                                                                           #Traverse nums backward.
            while stack and nums[stack[-1]] > nums[i]:                                                                 #While stack is not empty the number at the index on top of stack is greater than current number, pop stack.
                left[stack.pop()] = i                                                                                  #Set the left of that number to i.
            stack.append(i)                                                                                            #Append i to stack.
        right = [len(nums)] * len(nums)                                                                                #For each number, store the first index to the right that is smaller than current number; initially it's len(nums) means no smaller number to the right. 
        stack = []                                                                                                     #Use a stack to store indexes whose numbers are in increasing order.
        for i in range(len(nums)):                                                                                     #Traverse nums forward.
            while stack and nums[stack[-1]] > nums[i]:                                                                 #While stack is not empty the number at the index on top of stack is greater than current number, pop stack.
                right[stack.pop()] = i                                                                                 #Set the right of that number to i.
            stack.append(i)                                                                                            #Append i to stack.
        return max(nums[i] * (right[i] - left[i] - 1) for i in range(len(nums)) if left[i] < k and right[i] > k)       #Find the max of score of each index i, if left[i] and right[i] is to the left and right of k respectively.
                                                                                                                       #So, the span is (right[i] - left[i] - 1) and all numbers in the span is at least nums[i].


    def maximumScore(self, nums: List[int], k: int) -> int:
        left, right = k, k                                                                                             #Initialize the left and right boundary of span both at k. 
        result, minValue = nums[k], nums[k]                                                                            #Initialize result and min value.
        while left > 0 or right < len(nums) - 1:                                                                       #Iterate while either left or right hasn't reach the end. 
            if (nums[left - 1] if left else 0) < (nums[right + 1] if right < len(nums) - 1 else 0):                    #If the number beyond left(0 if reaches end) is smaller than number beyond right(0 if reaches end), move right further and update minValue.
                right += 1                                                                                             #Because in this case, the new minValue should be greater than that of moving left, thus we won't miss a possible result and we will come back to pick up the result of moving left.
                minValue = min(minValue, nums[right])
            else:                                                                                                      #Otherwise, move left further and update minValue.
                left -= 1                                                                                              #Because in this case, the new minValue should be greater than that of moving right, thus we won't miss a possible result and we will come back to pick up the result of moving right.
                minValue = min(minValue, nums[left])
            result = max(result, minValue * (right - left + 1))                                                        #Calculate score and update result if necessary.
        return result
