class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        def commonSubsequence(array1: List[int], array2: List[int]) -> List[int]:      #Use 2 pointers to find the longest common subsequence in 2 sorted arrays.
            i, j = 0, 0
            result = []
            while i < len(array1) and j < len(array2):
                if array1[i] == array2[j]:
                    result.append(array1[i])
                    i += 1
                    j += 1
                elif array1[i] < array2[j]:
                    i += 1
                else:
                    j += 1
            return result

        result = arrays[0]                                                             #Initialize result to be the first array.
        for array in arrays[1:]:                                                       #Traverse the rest of arrays.
            result = commonSubsequence(result, array)                                  #Find the longest common subsequence between result and current array and set result to it.
        return result
