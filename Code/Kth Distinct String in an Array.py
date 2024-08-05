class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)      #Count each string.
        for x in arr:             #Traverse arr.
            if count[x] == 1:     #If x is distinct, decrease k.
                k -= 1
            if not k:             #If k is 0, x is the k-th distinct string.
                return x
        return ""                 #Return empty string if cannot find.
