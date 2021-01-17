class Solution:
    def countVowelStrings(self, n: int) -> int:
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) // 24  #Choose n digits from the pool of 5 digits with repetitions, a.k.a the n + 1 of Pentatope number, https://en.wikipedia.org/wiki/Pentatope_number.
