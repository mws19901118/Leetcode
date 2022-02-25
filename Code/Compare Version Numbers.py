class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        r1, r2 = version1.split('.'), version2.split('.')       #Split version1 and version2 by '.' to get r1 and r2 list.
        for i in range(max(len(r1), len(r2))):                  #Traverse r1 and r2 simutanously.
            x = int(r1[i]) if i < len(r1) else 0                #Get the current revision in version1; if i is out of bound of r1, set revision to 0.
            y = int(r2[i]) if i < len(r2) else 0                #Get the current revision in version2; if i is out of bound of r2, set revision to 0.
            if x < y:                                           #If x < y, version1 is smaller than version2.
                return -1
            elif x > y:                                         #If x > y, version1 is greater than version2.
                return 1
        return 0                                                #If all revisions are equal after traverse, version1 and version2 are equal.
