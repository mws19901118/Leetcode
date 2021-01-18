class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)                             #Count each number in nums.
        result = 0
        for x in c:                                   #Traverse the keys in counter.
            if k - x == x:                            #If 2 * x == k, and c[x] // 2 to result.
                result += c[x] // 2
            elif k - x in c:                          #Otherwise if k - x in c, add min(c[x], c[k - x]) to result.
                result += min(c[x], c[k - x])
                c[x] = 0                              #Set c[x] and c[k - x] to 0 because they have already been visited.
                c[k - x] = 0
        return result
