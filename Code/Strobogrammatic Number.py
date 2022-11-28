class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatic = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}                                                            #Define the strobogrammatic dict.
        return all(num[i] in strobogrammatic and num[-(i + 1)] == strobogrammatic[num[i]] for i in range((len(num) + 1) // 2))          #For all first half(including middle) characters, it should be in the dict and the corresponding character in second half should be strobogrammatic with it. 
