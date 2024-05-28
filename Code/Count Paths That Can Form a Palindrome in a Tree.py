class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        alphabet = set(s)                                                  #Get the distinct characters in s.
        adjacentList = defaultdict(list)                                   #Build adjacent list.
        for i, x in enumerate(parent):                                     #Traverse parent.
            adjacentList[x].append((i, s[i]))                              #For each node, append its child and character of corresponding edge to its adjacent list.
        masks = {x: 1 << (ord(x) - ord('a')) for x in alphabet}            #Initialize bit masks for each character.
        count = Counter()                                                  #Count each bit masks of string from root.
        result = 0                                                         #Initialize result.
        def dp(index: int, mask: int) -> None:                             #Traverse tree.
            nonlocal result
            result += count[mask]                                          #Add count[mask] to result since 2 strings with same mask can form a palindrome because all characters in concatenated string have even occurrence.
            result += sum(count[mask ^ masks[x]] for x in alphabet)        #Add the sum of count of strings whose bit mask is one bit away from current mask since 2 strings whose bit masks are 1 bit away can form a palindrome because the concatenated string will only have one character with odd occurrence.
            count[mask] += 1                                               #Increase count of current mask
            for x, y in adjacentList[index]:                               #Traverse the adjacent list of current node.
                dp(x, mask ^ masks[y])                                     #Keep dp in the children with updated mask.
        dp(0, 0)                                                           #Start dp from node 0 and empty bit mask.
        return result
