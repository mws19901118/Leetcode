class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def backtracking(index: int, count: Counter) -> int:
            if index == len(nums):                                                  #If index reaches the end, return 1 as we find a beautiful set.
                return 1
            result = backtracking(index + 1, count)                                 #Keep backtracking with not adding current number.
            if not count[nums[index] + k] and not count[nums[index] - k]:           #If current number plus k and current number minus k are both not in count, we can add current number.
                count[nums[index]] += 1                                             #Update current number count.
                result += backtracking(index + 1, count)                            #Keep backtracking.
                count[nums[index]] -= 1                                             #Restore current number count.
            return result                                                           #Return result.
        
        return backtracking(0, Counter()) - 1                                       #Return the result of backtracking from the begining, also minus 1 to remove the empty set.
