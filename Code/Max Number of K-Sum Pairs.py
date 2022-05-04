class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)                                                                                                   #Count each number in nums.
        return sum([(c[x] // 2) if k - x == x else min(c[x], c[k - x]) for x in c if x <= k - x and k - x in c])            #Traverse the keys in counter. If x < k - x, add min(c[x], c[k - x]) to result; if x == k - x, add c[x] // 2 to result.
