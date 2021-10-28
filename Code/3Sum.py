class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)                                                                                                             #Count nums.
        keys = sorted(list(counter.keys()))                                                                                                 #Sort unique numbers.
        result = []                                                                                                                         #Initialize result.
        for i, x in enumerate(keys):                                                                                                        #Traverse keys.
            for y in keys[i:]:                                                                                                              #Traverse keys[i:].
                if (x == y and counter[x] > 1) or x < y:                                                                                    #y has to be larger than x or equals to z and counter[x] > 1.
                    z = -(x + y)                                                                                                            #Compute z = -(x + y).
                    if z in counter and (y < z or (x < y and y == z and counter[z] > 1) or (x == y and y == z and counter[z] > 2)):         #If z in counte and (y < z or (x < y and y == z and counter[z] > 1) or (x == y and y == z and counter[z] > 2)), we found a triplet (x, y, z) which sums to 0.
                        result.append([x, y, z])
        return result                                                                                                                       #Return result.
