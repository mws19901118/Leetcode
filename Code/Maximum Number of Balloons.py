class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)                                                               #Count each character.
        return min(count['b'], count['a'], count['l'] // 2, count['o'] // 2, count['n'])    #Return the min possible value.
