class Solution:
    def checkRecord(self, n: int) -> int:
        division = 10 ** 9 + 7                                                          #Initialize division.
        count = [[1, 2, 2], [2, 3, 3]]                                                  #Use a 2 * 3 matrix to store number of current length given A allowed and L allowed at end; each value is initialized with 1, then plus 1 if A is allowed and plus 1 if more than 0 L is allowed.   
        for _ in range(n - 1):                                                          #Iterate n - 1 times.
            newCount = [[count[0][2]] * 3, [count[1][2]] * 3]                           #Initialize newCount to have P for today; then 2 L are allowed from previous cunt but A is not changed.
            for j in range(3):                                                          #Update newCount for 1 A is allowed by adding 2 L are allowed but 0 A is allowed from previous count.
                newCount[1][j] = (newCount[1][j] + count[0][2]) % division
            for i, j in product(range(2), range(1, 3)):                                 #Update newCount for more than 0 L is allowed by adding less one L is allowed from previous count.
                newCount[i][j] = (newCount[i][j] + count[i][j - 1]) % division
            count = newCount                                                            #Replace count with newCount.
        return count[1][2]                                                              #Return the final count when A is allowed and 2 L are allowed.
