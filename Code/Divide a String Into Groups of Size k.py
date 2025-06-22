class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        return [s[i:i + k] + fill * max(0, i + k - len(s)) for i in range(0, len(s), k)]      #Divide and fill the lasat one if necessary.
