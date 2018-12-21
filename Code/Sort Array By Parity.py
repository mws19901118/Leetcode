class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for a in A:
            if a % 2:             #Find all odd values.
                odd.append(a)
            else:                 #Find all even values.
                even.append(a)
        return even + odd         #Add odd at the end of even and return.
