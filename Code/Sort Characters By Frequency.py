class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)                                                     #Count each character.
        characters = sorted(list(count.keys()), key = lambda x: -count[x])      #Sort characters in desending order by its count.
        return "".join([x * count[x] for x in characters])                      #Join the segments(each character duplicated by its count) together and return.
