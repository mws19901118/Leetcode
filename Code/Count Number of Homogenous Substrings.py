class Solution:
    def countHomogenous(self, s: str) -> int:
        division = 10 ** 9 + 7                                                #Initialize division.
        i, count = 0, 0                                                       #Initialize first pointer and count.
        while i < len(s):                                                     #Traverse s with 2 pointers.
            j = i + 1
            while j < len(s) and s[j] == s[i]:                                #Move second pointer while its value is same with first pointer.
                j += 1
            count = (count + (j - i) * (j - i + 1) // 2) % division           #For a substring consists only by one character with length n, there are n * (n + 1) // 2 total homogenous substrings.
            i = j
        return count                                                          #Return count.
