class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()                                        #Store all bitwise OR results.
        current_or = {0}                                      #Store the bitwise OR results of subarrays ending at current index; initially it only has 0.
        for x in arr:                                         #Traverse arr.
            current_or = {x | y for y in current_or} | {x}    #Update current_or by applying bitwise OR operations on each number in current_or and x. Also add x to it if it is not already there.
            result |= current_or                              #Union result with current_or.
        return len(result)                                    #Return the length of result
