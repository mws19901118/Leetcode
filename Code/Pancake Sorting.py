class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        result = []
        for i in range(len(A), 0, -1):                                              #Traverse from len(A) to 1.
            index = A.index(i)                                                      #Find the index of i in A.
            result.append(index + 1)                                                #Pancake flip the elements from the beginning to the index.
            A = A[:index + 1][::-1] + A[index + 1:]
            result.append(i)                                                        #Pancake flip the elements from the beginning to i.
            A = A[:i][::-1] + A[i:]
        return result
