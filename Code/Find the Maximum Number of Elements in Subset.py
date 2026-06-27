class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)                                                          #Count each number.
        result = 0
        for x in count:                                                                #Traverse each unique number.
            if x == 1:                                                                 #If x == 1, we can make the array with max odd number of 1.
                result = max(result, count[x] if count[x] & 1 else (count[x] - 1))
                continue                                                               #Skip the rest.
            length, curr = 0, x                                                        #Initialize length and curr.
            while count[curr] >= 2:                                                    #Iterate while count[curr] >= 2.
                length += 2                                                            #Increase length by 2 to put curr on symmetric postions.
                curr **= 2                                                             #Move curr to curr ** 2.
            length += (1 if count[curr] == 1 else -1)                                  #If count[curr] == 1, we can put it in the middle; otherwise we have to remove 1 of the middle numbers.
            result = max(result, length)                                               #Update result if necessary.
        return result
