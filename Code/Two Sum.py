class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = defaultdict(list)
        for i, x in enumerate(nums):                                    #Store indexes of each number in a dictionary.
            indexes[x].append(i)
        for i, x in enumerate(nums):                                    #Traverse nums.
            if target - x in indexes:                                   #If target - x is in indexes, we have a potential 2 sum pair.
                if target - x == x and len(indexes[x]) > 1:             #If target - x == x, then it requires at least 2 occurence of x to make a valid pair.
                    return [indexes[x][0], indexes[x][1]]
                elif target - x != x:                                   #If target - x != x, return [i, indexes[target - x][0]] as a valid pair.
                    return [i, indexes[target - x][0]]
