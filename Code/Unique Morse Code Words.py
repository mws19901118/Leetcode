class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]          #Morse code.
        s = {"".join([morse[ord(x) - ord('a')] for x in w]) for w in words}                                                                                                                                         #Covert each word to morse code and de-dupe in a set.
        return len(s)                                                                                                                                                                                               #Return the length of set.
