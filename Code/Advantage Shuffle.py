class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()                                                              #Sort A.
        sortedBWithIndex = sorted([(x, i) for i, x in enumerate(B)])          #Sort B and keep index with value.
        result = [-1] * len(A)                                                #Initialize result.
        start, end = 0, len(A) - 1                                            #Store 2 end of unmatched elements. the index of min and max unmatched elements in B.
        for x in A:                                                           #Traverse A.
            if x > sortedBWithIndex[start][0]:                                #If x is larger than the min unmatched element in B, match it with x.
                result[sortedBWithIndex[start][1]] = x
                start += 1
            else:                                                             #Otherwise it can not gain any advantage anyway, so match the max unmatch element in B with x and save us a larger number.
                result[sortedBWithIndex[end][1]] = x
                end -= 1
        return result
