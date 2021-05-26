class Solution:
    def toLowerCase(self, s: str) -> str:
        gap = ord('a') - ord('A')                                                                   #Get the distance in ASCII for lower case character and upper case character.
        return "".join([chr(ord(x) + gap) if ord('A') <= ord(x) <= ord('Z') else x for x in s])     #Convert each upper case character to lower case and return.
