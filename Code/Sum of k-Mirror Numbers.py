class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def isKMirror(x: int) -> bool:                                                        #Convert x to digits in k-base and check if it is palindrome.
            digits = []
            while x:
                digits.append(x % k)
                x //= k
            return digits == digits[::-1]

        left, result = 1, 0                                                                   #Initialize start of traverse and result.
        while n:                                                                              #Iterate until found first n k-mirror numbers.
            for op in [0, 1]:                                                                 #Try 2 ways of generating palindrome: 0 is reversing number without last digit while 1 is reversing entire number.
                for i in range(left, left * 10):                                              #Traverse from left to left * 10, basically all numbers at current length.
                    if not n:                                                                 #If already found n k-mirror numbers, break.
                        break
                    half = str(i // 10 if not op else i)                                      #Get the first half based on way of generating palindrome.
                    palindrome = int(str(i) + ("" if half == "0" else half[::-1]))            #Generating palindrome(don't attach reversed first half if half is 0).
                    if isKMirror(palindrome):                                                 #If it is k-mirror number, add it to result and decrease n.
                        n -= 1
                        result += palindrome
            left *= 10                                                                        #Move to next length.

        return result
