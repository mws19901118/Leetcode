class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half = (intLength + 1) // 2                             #Calculate the length of first half of the palindrome.
        start = 10 ** (half - 1)                                #The start of first half is 10 ** (half - 1).

        def getPalindrome(i: int):                              #Get the palindrome for query.
            firstHalf = str(i - 1 + start)                      #The first half of i-th palindrome is i - 1 + start.
            if len(firstHalf) > half:                           #If its length is longer than half, it exceeds the boundary, meaning there is not enough palindrome, so it should return -1.
                return -1 
            if intLength % 2:                                   #If the intLength is odd, reverse the first half excluding last digit and append the reversed to firstHalf; convert to int and return.
                return int(firstHalf + firstHalf[-2::-1])
            else:                                               #Otherwise, reverse the first half and append the reversed to firstHalf; convert to int and return. 
                return int(firstHalf + firstHalf[::-1])
            
        return [getPalindrome(x) for x in queries]              #Return the list of palindrome for each query.
