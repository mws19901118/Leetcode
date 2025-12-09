class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        result, division = 0, 10 ** 9 + 7                                                                                      #Initialize result and division.
        currCount, totalCount = Counter(), Counter(nums)                                                                       #Initialize current count of each number and calculate the total count of each number.
        for i, x in enumerate(nums):                                                                                           #Traverse nums.
            result = (result + currCount[x * 2] * (totalCount[x * 2] - currCount[x * 2] - int(x == x * 2))) % division         #On the left, left there are currCount[x * 2] of x * 2, while on the right, there are totalCount[x * 2] - currCount[x * 2] - int(x == x * 2)) x * 2. So update result accordingly.
            currCount[x] += 1                                                                                                  #Update current count of x.
        return result
