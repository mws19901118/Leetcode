class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        next_chr = {x: chr((ord(x) - ord('a') + 1) % 26 + ord('a')) for x in 'abcdefghijklmnopqrstuvwxyz'}    #Build the next character map for each character from a to z.
        index = 0                                                                                             #Initialize a pointer to traverse str2.
        for i, x in enumerate(str1):                                                                          #Traverse str1.
            if index < len(str2) and (x == str2[index] or next_chr[x] == str2[index]):                        #If hasn't reach the end of str2 also either x or next_chr[x] is same as str2[index], we found a match for str2[index], so move forward index.
                index += 1
        return index == len(str2)                                                                             #Return if reaches the end of str2.
