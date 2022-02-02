class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        diff = [0] * 26                                               #Maintain the diff of letter count between running window in s and p.
        for x in p:                                                   #Initialize the diff(letter count of p) and count.
            diff[ord(x) - ord('a')] += 1
        count = sum(x != 0 for x in diff)                             #Count the number of letters not match.
        result = []
        for i in range(len(s)):
            diff[ord(s[i]) - ord('a')] -= 1                           #Update diff and count everytime the running window has a new letter.
            count -= diff[ord(s[i]) - ord('a')] == 0
            if count == 0:                                            #If no not matched letter between running window and p, an anagram is found, so append the current starting index of running window to result list. 
                result.append(i - len(p) + 1)                         
            if i >= len(p) - 1:                                       #Pop current starting index out of running window if its length is len(p) and update diff and count if necessary.
                count += diff[ord(s[i - len(p) + 1]) - ord('a')] == 0
                diff[ord(s[i - len(p) + 1]) - ord('a')] += 1
        return result
