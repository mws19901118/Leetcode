class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = [], []                #Separate array into a positive array and a negative array.
        for x in nums:
            if x > 0:
                positive.append(x)
            else:
                negative.append(x)
        i = 0
        for x, y in zip(positive, negative):      #Merge 2 ararys.
            nums[i] = x
            nums[i + 1] = y
            i += 2
        return nums
