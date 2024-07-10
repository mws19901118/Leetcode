class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0                                #Count the folder level.
        for x in logs:                           #Traverse logs.
            if x == "./":                        #If x == "./", do nothing.
                continue
            elif x == "../":                     #If x == "../", do to upper level if not in main folder; otherwise, stay in main folder.
                count = max(count - 1, 0)
            else:                                #Otherwise, go into the folder.
                count += 1
        return count
