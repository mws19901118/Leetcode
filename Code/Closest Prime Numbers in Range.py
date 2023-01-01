class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = [True] * (right + 1)                                                    #Initialize a list of boolean for length (right + 1), meaning if the number of index is prime.
        num1, num2, result = None, None, None                                             #Initialize num1, num2 and result all to be none.
        for i in range(2, right + 1):                                                     #Traverse from 2 to right.
            if not isPrime[i]:                                                            #If i is not prime, skip.
                continue
            for j in range(i * 2, right + 1, i):                                          #Set all numbers which are multiples of i, excluding i itself, and not greater than right to not prime.
                isPrime[j] = False
            if i >= left:                                                                 #If i is greater than or equal to left, we try to find num1 and num2.
                if num1:                                                                  #If num1 is already found, set num2 to i.
                    num2 = i
                    if not result or (num2 - num1) < (result[1] - result[0]):             #Update result to [num1, num2] if it is none or (num2 - num1) < (result[1] - result[0]).
                        result = [num1, num2]
                num1 = i                                                                  #Update num1 to i.
        return [-1, -1] if not result else result                                         #Return [-1, -1] if result is none; otherwise return result.
