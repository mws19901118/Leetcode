class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        count = defaultdict(int)
        for i in range(len(s) - 9):                         #Count sequences.
            count[s[i:i+10]] += 1
        return [x for x in count if count[x] > 1]           #Return sequences whose count is larger than 1.
