class Solution:
    def findIntegers(self, n: int) -> int:
        fibonacci = [1, 2]                                            #There are 2 integers(0 and 1) without consecutive ones whose binary length is 1; and for binary length 0, set a dummy count to 1.
        for i in range(2, 32):                                        #Since 10 ** 9 is at most 32 bits in binary, we traverse from 2 to 32.
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])     #To generate all integers without consecutive ones whose binary length is n, we can add '0' to those whose binary length is n - 1 and add '01' to those whose binary length is n - 2.
        count, prev = 30, 0, 0                                        #Intialize total of integers without consecutive ones and previous bit.
        binary = format(n, '032b')                                    #Convert n to 32 bit binary string.
        for i in range(32):                                           #Traverse from most significant bit to lowest significant bit.
            if binary[i] == '1':                                      #If current bit is '1', let's first fix '0' at currebt bit, so it will be A0B. A has i bits and B has 31 - i bits. For each integer without consecutive ones X whose binary length is 31 - i, A0X is without consecutive ones and smaller than n. Then fix '1' at current bit.
                count += fibonacci[31 - i]                            #So, add fibonacci[31 - i] to count.
                if prev == 1:                                         #If previous bit is also 1, n is not an integer without consecutive ones.
                    count -= 1
                    break                                             #Add stop traverse as we cannot find any larger integers without consecutive ones. Because that will trigger the change to change current bit to '1', which is confilct with previous '1'.
                prev = 1
            else:                                                     #If current bit is '0', set prev to 0 and we cannot add more integers for now.
                prev = 0
        return count + 1                                              #Return count + 1 as n itself(deducted one already if n is not).
