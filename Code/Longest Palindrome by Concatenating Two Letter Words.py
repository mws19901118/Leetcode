class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)                                    #Count each word.
        matched = set()                                           #Use set to store match palindromes.
        length, middle = 0, 0                                     #Initialize the palindrome length and if we can add a final palindrome in the middle.
        for x in count:                                           #Traverse unique word.
            if x in matched:                                      #If it's already matched, skip.
                continue
            if x[0] == x[1]:                                      #If the 2 letters in x is same, add (count[x] // 2) pairs of palindrome to final length.
                length += (count[x] // 2) * 4
                middle |= count[x] % 2                            #If count[x] % 2, we can add a final palindrome in the middle.
            elif x[::-1] in count:                                #Otherwise, add min(count[x], count[x[::-1]]) pairs of palindrome to final length.
                length += min(count[x], count[x[::-1]]) * 4
                matched.add(x[::-1])                              #Mark x[::-1] as matched.
        return length + middle * 2                                #Return length + middle * 2.
