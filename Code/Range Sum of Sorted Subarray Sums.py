class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        newArray = []                                              #Initialize subarray sum arary.
        for i in range(n):                                         #Enumerate the starting index of each subarray.
            subarraySum = 0
            for x in nums[i:]:                                     #Traverse nums[i:], update subarray sum.
                subarraySum += x
                newArray.append(subarraySum)                       #Append subarray sum to new array.
        newArray.sort()                                            #Sort new array.
        return sum(newArray[left - 1:right]) % (10 ** 9 + 7)       #Sum up from index left - 1 to right - 1, then take modulo by 10 ** 9 + 7.
