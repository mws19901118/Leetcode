class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = []                          #Initialize result.
        count = Counter(nums)                #Count each number in nums.
        s = set(count.keys())                #Store all number in a set.
        while s:                             #Iterate while s is not empty.
            row = []                         #Initialize row.
            for x in count:                  #Traverse all number in count.
                if x not in s:               #If x is not in set, continue.
                    continue
                row.append(x)                #Append x to rpw.
                count[x] -= 1                #Decrese its count.
                if not count[x]:             #If its count is 0, remove it from set.
                    s.remove(x)
            result.append(row)               #Append row to result.
        return result
