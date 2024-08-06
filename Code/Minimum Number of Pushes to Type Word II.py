class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(x * ceil((i + 1) / 8) for i, x in enumerate(sorted(Counter(word).values(), reverse = True)))      #Count each character, then sort count in desending order. Try to map characters with higher count to the first of each button. Since there are only 8 buttons, so the i-th character requires ceil((i + 1) / 8) button pushes. 
