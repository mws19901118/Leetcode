class Solution:
    def punishmentNumber(self, n: int) -> int:
        @cache                                                                        #Cache result.
        def partition(s: str, x: int) -> bool:                                        #Determine if s can be partitioned with sum x.
            if not s and not x:                                                       #If s is empty string and x is 0, return true as no more partition needed.
                return True
            can_partition, i = False, 0                                               #Initialize can_partition and i.
            while not can_partition and i < len(s) and x - int(s[:i + 1]) >= 0:       #Iterate while can not partition and i haven't reached the end and remain is greater than 0.
                can_partition |= partition(s[i + 1:], x - int(s[:i + 1]))             #If s[i + 1:] can be partitioned with sum x - int(s[:i + 1]), then s can be partitioned with sum x.
                i += 1
            return can_partition                                                      #Return can_partition.
        return sum(i * i for i in range(1, n + 1) if partition(str(i * i), i))        #Sum up i * i for all i from 1 to n that i * i can be partitioned with sum i.
