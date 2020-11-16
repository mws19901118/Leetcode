class Solution:
    def longestMountain(self, A: List[int]) -> int:
        i, result = 0, 0                                            #Initalize pointer and result.
        while i < len(A) - 1:                                       #Start traversing through A.
            j = i + 1
            while j < len(A) and A[j] > A[j - 1]:                   #Find the uphill of a mountain.
                j += 1
            if j > i + 1 and j < len(A) and A[j] < A[j - 1]:        #Check if it's a valid uphill of a mountain(longer than 1, not reaching the end and there is a downhill right after it).
                k = j
                while k < len(A) and A[k] < A[k - 1]:               #Find the downhill of a moutain.
                    k += 1
                if k > j:                                           #If it's a valid downhill of a mountain(longer than 1), update the max length.
                    result = max(result, k - i)
                i = k - 1                                           #Move i to the end of down hill, k - 1.
            else:
                i = j                                               #Move i to j.
        return result
