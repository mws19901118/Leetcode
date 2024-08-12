class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        #(a & b) ^ (a & c) = (!(a & b) & (a & c)) | ((a & b) & !(a & c)) = ((!a | !b) & a & c) | (a & b & (!a | !b))
        #Since !a and a cannot both be true at same time, so !b and !c is true.
        #((!a | !b) & a & c) | (a & b & (!a | !b)) = (!b & a & c) | (a & b & !c) = a & ((!b & c) | (b & !c)) = a & (b ^ c)
        #Next, if the length of arr1, arr2 is m and n respectively, for 0 <= i < m, (arr1[i] & arr2[0]) ^ (arr1[i] & arr2[1]) ^ ... ^ (arr1[i] & arr2[n - 1]) = arr1[i] & (arr2[0] ^ arr2[1] ^ ... ^ arr2[n - 1]).
        #Then, let (arr2[0] ^ arr2[1] ^ ... ^ arr2[n - 1]) be X, the final result is (arr1[0] & X) ^ (arr1[1] & X) ^ ... ^ (arr1[m - 1] & X) =  (arr1[0] ^ arr1[1] ^ ... ^ arr1[m - 1]) & X.
        #So, calculate the XOR result of each array and take the and result from those 2.
        return reduce(lambda x, y: x ^ y, arr1) & reduce(lambda x, y: x ^ y, arr2)
      
