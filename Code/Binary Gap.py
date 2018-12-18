class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = bin(N)[2:]                 #Covert to binary in string and ignore the '0b' prefix.
        dis = 0
        i = 0
        last = 0
        for i in range(len(binary)):        #Find the longest distance in one pass.
            if binary[i] == '1':
                dis = max(i - last, dis)
                last = i
        return dis     
