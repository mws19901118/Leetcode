class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xorResult = 0                                                                                      #Initialize xor result.
        xorResultIndexes = defaultdict(list)                                                               #Store the ending indexes for subarrays starting from beginning by the xor result of subarray.
        xorResultIndexes[0].append(-1)                                                                     #Initially, it is 0 at -1.
        result = 0                                                                                         #Initialize result.
        for i, x in enumerate(arr):                                                                        #Traverse arr.
            xorResult ^= x                                                                                 #Calculate xor result for current subarray.
            result += sum(max(0, i - index - 1) for index in xorResultIndexes[xorResult])                  #To find the triplet, it is equivelent to find a sunarry whose xor result is 0, because a == b, then we can split the subarray at any place except its start(becase i < j) to 2 halfs and the xor result of each half equals. And for any index in xorResultIndexes[xorResult], xor result of arr[index + 1:i + 1] is 0.
            xorResultIndexes[xorResult].append(i)                                                          #Append i to xorResultIndexes[xorResult].
        return result
