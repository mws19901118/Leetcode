class Solution:
    def grayCode(self, n: int) -> List[int]:
        code = [0, 1]                           #Initialize gray code for n = 1.
        mask = 1                                #Initialize mask to be 2 ** (n - 1).
        for i in range(2, n + 1):               #Generate gray codes from 2 to n.
            mask <<= 1                          #Left shift mask by 1 bit to make it 2 ** (i - 1). 
            for j in reversed(range(mask)):     #Traverse backwards the gray code from i - 1, whose length equals mask.
                code.append(code[j] | mask)     #Append code[j] | mask to code, to form the gray code of i. The second half of gray code is the reverse of first half with the most significant bit is 1.
        return code
