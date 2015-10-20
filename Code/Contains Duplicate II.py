class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dict={}                               #The keys of dict are values of elements in nums; the values of dict are a list storing the indexes of elements which have the same value.
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]]=[i]             #Initialize the list.
            else:
                if i-dict[nums[i]][-1]<=k:    #If there the distance between current index and last index is not larger than k, return true.
                    return True
                else:
                    dict[nums[i]].append(i)
        return False
