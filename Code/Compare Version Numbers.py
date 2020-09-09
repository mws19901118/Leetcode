class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(v) for v in version1.split(".")]                  #Covert version 1 to a list of number.
        v2 = [int(v) for v in version2.split(".")]                  #Covert version 2 to a list of number.
        i, j = 0, 0
        while i < len(v1) and j <len(v2):                           #Compare the version numbers of same index in version1 and version2 respectively.
            if v1[i] < v2[j]:                                       #If version number in version1 is smaller than that in version2, return -1.
                return -1
            elif v1[i] > v2[j]:                                     #If version number in version1 is larger than that in version2, return 1.
                return 1
            else:                                                   #Otherwise, move to next index.
                i += 1
                j += 1
        if i < len(v1):                                             #If v1 hasn't reached end, if there are version numbers that are not 0, return 1; otherwise return 0.
            return int(any(x != 0 for x in v1[i:]))
        else:                                                       #If v2 hasn't reached end, if there are version numbers that are not 0, return -1; otherwise return 0.
            return -int(any(x != 0 for x in v2[j:]))
