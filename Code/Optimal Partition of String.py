class Solution:
    def partitionString(self, s: str) -> int:
        i, partitions = 0, 0
        while i < len(s):                                     #Traverse s with 2 pointers.
            j = i
            window = set()                                    #Initialize a set to store unique characters in current window.
            while j < len(s) and s[j] not in window:          #While s[j] not in window, add s[j] to window and move forward j.
                window.add(s[j])
                j += 1
            partitions += 1                                   #Increase partitions.
            i = j
        return partitions
