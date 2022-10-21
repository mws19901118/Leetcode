class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = defaultdict(lambda: -1)                           #Use default dict to store last indexes of each value.
        for i, x in enumerate(nums):                                #Traverse nums.
            if indexes[x] != -1 and i - indexes[x] <= k:            #If indexes[x] != -1 and i - indexes[x] <= k, return true.
                return True
            indexes[x] = i                                          #Set indexes[x] to i.
        return False                                                #Return false.
