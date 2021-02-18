class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count = 0
        i = 0
        while i < len(A) - 2:                                           #Traverse the possible start of arithmetic sequence. Because minimal length is 3, so the max index of start is len(A) - 3.
            j = i + 1                                                   
            while j < len(A) and A[j] - A[j - 1] == A[i + 1] - A[i]:    #Find the end of current arithmetic sequence.
                j += 1
            length = j - i                                              #Calculate the length of arithmetic sequence.
            count += (length - 2) * (length - 1) // 2                   #Calculate total slices in current sequence.
            i = j - 1                                                   #Move start to next possible start, which is the end of current arithmetic sequence.
        return count                                                    #Return count.
