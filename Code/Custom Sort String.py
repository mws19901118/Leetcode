class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderSet = set(x for x in order)            #Store characters in order in a set.
        count = Counter(s)                          #Count each character in s.
        result = ""
        for x in order:                             #Append each character(all occurances) in s that is in order.
            result += x * count[x]
        for x in count:                             #Append the charcters(all occurances) in s that is not in order
            if x not in orderSet:
                result += x * count[x]
        return result
