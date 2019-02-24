class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        count = collections.Counter()         #Use a counter to count the appearance of number in sliding window.
        result = 0
        length = 0                            #For each index i, length represents the distance between the first j and last j than A[j]...A[i] is a subarray with K different integers.
        j = 0                                 #The left bound of sliding window.
        for i in range(len(A)):
            count[A[i]] += 1                  #For each index i, add 1 to the count of A[i].
            if len(count) < K:                #If count has less than K entries, subarray A[j]...A[i] does not have K different integers yet, so continue.
                continue
            elif len(count) == K:             #If count has K entries, subarray A[j]...A[i] has K different integers for the first time or is extending a such subarray.
                length = max(length, 1)       #So, length should be the max of previous length and 1.
            else:                             #If count has more than K entries, subarray A[j]...A[i] has K + 1 different integers.
                del count[A[j]]               #Remove A[j] from count.
                j += 1                        #j goes to the next.
                length = 1                    #Refresh length.
            while count[A[j]] != 1:           #The last j for A[i] should be the first integer in sliding window whose count is 1. For k > last j, A[k]...A[i] does not have enough K different integers.
                length += 1                   #While j goes forward, increase length by 1.
                count[A[j]] -= 1              #Decrease count[A[j]], since current j is already out of sliding window.
                j += 1
            result += length                  #Add length to result.
        return result                         #Return result.
