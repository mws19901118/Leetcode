class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = Counter(nums)                                      #Count each number.
        non_distinct_nums = sum(count[x] > 1 for x in count)       #Count non distinct nunbers.
        index = 0                                                  #Initialize index.
        while index < len(nums) and non_distinct_nums > 0:         #Iterate while index hasn't reached the end and there are still non distinct numbers.
            for x in nums[index:min(index + 3, len(nums))]:        #Remove the 3 numbers after index(or all numbers if they are fewer than 3 numbers.)
                count[x] -= 1
                if count[x] == 1:                                  #If current number only has 1 count now, decrease count of non distinct numbers.
                    non_distinct_nums -= 1
            index += 3                                             #Move forward index by 3.
        return index // 3                                          #Return index // 3 as the number of operations.
