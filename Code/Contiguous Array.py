class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0                                                         #Count the number of unmatched 0 from beginning.
        firstApperance = {0: -1}                                          #Store the index of first apperance of count value, initially count is 0 so first appearance is -1.
        maxLength = 0
        for i, x in enumerate(nums):
            if x == 0:                                                    #If current number is 0, increase count by 1; otherwise decrease it by 1.
                count += 1
            else:
                count -= 1
            if count in firstApperance:                                   #If count has appeared before, we found a contiguous array with equal number of 0 and 1.
                maxLength = max(maxLength, i - firstApperance[count])     #Calculate the length and if it's longer than current longest contiguous array, update max length.
            else:                                                         #Otherwise, add count value and current index to the dict.
                firstApperance[count] = i
        return maxLength
