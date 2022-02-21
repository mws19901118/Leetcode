class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority, count = None, 0                           #Initialize majority and count.
        for x in nums:                                      #Traverse nums.
            if count == 0 or x == majority:                 #If current count is 0 or x equals majority, set majority to x and increase count.
                majority = x
                count += 1
            else:                                           #Otherwise decrease count.
                count -= 1
        return majority                                     #Return majority.
