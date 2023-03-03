class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):            #Traverse haystack and find needle.
            if needle == haystack[i:i + len(needle)]:
                return i
        return -1                                                   #Return -1 if not found.
