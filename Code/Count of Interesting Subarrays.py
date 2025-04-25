class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        visited = Counter()                         #Store the visited times of remain of count of indexes satisfying condition divided by modulo
        visited[0] = 1                              #Initially, count is 0.
        result, count = 0, 0                        #Initialize result and count.
        for i, x in enumerate(nums):                #Traverse nums.
            count += (x % modulo == k)              #Update the count of indexes satisfying condition from start to i(inclusive).
            r = count % modulo                      #Calculate the remain of count divided by modulo.
            result += visited[(r - k) % modulo]     #For all indexes j at which the remain of count by modulo is (r - k) % modulo, nums[i:j] is an interesting subarray.
            visited[r] += 1                         #Increase visited times of the remain current count divided by modulo.
        return result
