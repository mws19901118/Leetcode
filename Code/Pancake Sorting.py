class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(A)):
            index = A.index(i + 1, 0, len(A) - i)                               #Find the index of (i + 1) in A.
            if index == len(A) - 1 - i:                                         #If it's already the last (i + 1)th element in A, then the subarray starting from (i + 1) is already sorted from largest to smallest.
                continue                                                        #We don't need to do pancake flip. Continue.
            result.append(index + 1)                                            #Pancake flip the elements from the beginning to the index of (i + 1).
            for j in range((index + 1) / 2):                                    #After the flip, (i + 1) is the first element of A.
                A[j], A[index - j] = A[index - j], A[j]
            result.append(len(A) - i)                                           #Pancake flip the elements from the beginning to the last (i + 1)th element.
            for j in range((len(A) - i) / 2):                                   #After the flip, the subarray starting from (i + 1) is already sorted from largest to smallest.
                A[j], A[len(A) - 1 - i - j] = A[len(A) - 1 - i - j], A[j]
        
        result.append(len(A))                                                   #In the end, pancake flip the entire list, so it turns from sorted from largest to smallest to sorted from smallest to largest.
        return result
