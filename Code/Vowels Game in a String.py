class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(x in 'aeiou' for x in s)       #The only winning scenario for Bob is no vowels.
                                                  #If there are odd vowels, Alice just take the whole string.
                                                  #If there are even vowels, Alice can only leave 1 wowel to Bob. Bob either is out of move(the left vowel is the only character) or can only take a non-vowel character then let Alice takes the rest.
