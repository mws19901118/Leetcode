class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)            #Count each element.
        result = 0                       #Initialize result.
        for k, v in count.items():       #Traverse each element and its count.
            if v == 1:                   #If count is 1, the element cannot be deleted, so return -1.
                return -1
            result += ceil(v / 3)        #If v == 3 * i, the element can be deleted with i 3-delete operation; if v == 3 * i + 1, the element can be deleted with i - 1 3-delete operation and 2 2-delete operation; if v == 3 * i + 2, the element can be deleted with i 3-delete operation and 1 2-delete operation.
        return result
