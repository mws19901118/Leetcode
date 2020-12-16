class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        minAbs = 10001
        minAbsIndex = -1
        for i, x in enumerate(nums):                                                            #Find the element in A with min abs value and its index.
            if abs(x) < minAbs:
                minAbs = abs(x)
                minAbsIndex = i
        left, right = minAbsIndex - 1, minAbsIndex + 1                                          #Left pointer, traverse to the left of index and right pointer, traverse to the right of index.
        squares = [minAbs * minAbs]                                                             #Add the square of minAbs to the squares list.
        while left >= 0 or right < len(nums):
            if left >= 0 and (right >= len(nums) or abs(nums[left]) <= abs(nums[right])):       #If right pointer reaches the right end or the abs value of right pointer is not smaller than that of left pointer, add the square of value of left pointer to the squares list.
                squares.append(nums[left] * nums[left])
                left -= 1
            else:                                                                               #Otherwise, add the square of value of right pointer to the squares list.
                squares.append(nums[right] * nums[right])
                right += 1
        return squares
