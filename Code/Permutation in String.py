class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        diff = [0] * 26                                                       #Maintain the diff of letter count between running window in s2 and s1.
        count = 0                                                             #Count the number of letters not match.
        for x in s1:                                                          #Initialize the diff(letter count of s1) and count.
            count += diff[ord(x) - ord('a')] == 0
            diff[ord(x) - ord('a')] += 1
        for i in range(len(s2)):
            diff[ord(s2[i]) - ord('a')] -= 1                                  #Update diff and count everytime the running window has a new letter.
            count -= diff[ord(s2[i]) - ord('a')] == 0
            if count == 0:                                                    #If no not matched letter between running window and s1, an anagram is found, return true. 
                return True
            if i >= len(s1) - 1:                                              #Pop current starting index out of running window if its length is len(s1) and update diff and count if necessary.
                count += diff[ord(s2[i - len(s1) + 1]) - ord('a')] == 0
                diff[ord(s2[i - len(s1) + 1]) - ord('a')] += 1
        return False
