class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def halfToPalindrome(left: int) -> int:                                                                          #Generate a palindrome number based on the left part.
            s = str(left)                                                                                                #Convert left to string.
            mid = s[-1] if len(n) & 1 else ""                                                                            #We need a mid digit which is s[-1] if the length of n is odd.
            length = len(n) // 2                                                                                         #We will take the first len(n) // 2 digits of s.
            return int(s[:length] + mid + s[:length][::-1])                                                              #Append mid and reversed s[:length] to s[:length] then return.

        firstHalf = int(n[:(len(n) + 1) // 2])                                                                           #Calculate the first half, including the middle digit if length of n is odd.
        candidates = [halfToPalindrome(firstHalf), halfToPalindrome(firstHalf + 1), halfToPalindrome(firstHalf - 1)]     #All palindromes generated from firstHalf, firstHalf - 1 and firstHalf + 1 are candidates.
        candidates.append(10 ** (len(n) - 1) - 1)                                                                        #Also the last palindrome whose length is len(n) - 1.
        candidates.append(10 ** len(n) + 1)                                                                              #Also the first palindrome whose length is len(n) + 1.
        candidates.sort()                                                                                                #Sort candidates.
        diff, result, num = inf, 0, int(n)                                                                               #Initialize diff, result and convert n to int.
        for x in candidates:                                                                                             #Traverse candidates.
            if x == num:                                                                                                 #If x equals num, continue.
                continue
            if abs(x - num) < diff:                                                                                      #Update result and diff if current number has smaller diff from num.
                diff = abs(x - num)
                result = x
        return str(result)                                                                                               #Convert result to string and return.
