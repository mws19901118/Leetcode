class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        indexes = defaultdict(list)                                #Store the indexes of each number.
        for i, x in enumerate(nums):
            indexes[x].append(i)
        result = inf                                               #Initialize result.
        for i, x in enumerate(nums):                               #Traverse nums.
            y = int(str(x)[::-1])                                  #Calculate the reverse number of x.
            if y not in indexes:                                   #If y is not in indexes, skip.
                continue
            index = bisect_right(indexes[y], i)                    #Find the rightmost index to insert i in indexes[y].
            if index < len(indexes[y]):                            #If such index is not out of bound, j is indexes[y[[index], so update result if j - i is smaller.
                result = min(result, indexes[y][index] - i)
        return result if result < inf else -1                      #Return result if it is smaller than infinity; otherwise, return -1.
