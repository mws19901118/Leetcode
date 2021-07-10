class Solution:
    def numDecodings(self, s: str) -> int:
        division = 10 ** 9 + 7
        decodeMap = defaultdict(int)                                                                            #Store ways to decode in dict by letters..
        decodeMap["*"] = 9                                                                                      #Decode "*".
        decodeMap["1*"] = 9                                                                                     #Decode "1*".
        decodeMap["2*"] = 6                                                                                     #Decode "2*".
        decodeMap["**"] = 15                                                                                    #Decode "**".
        for i in range(1, 27):                                                                                  #Decode normal letters.
            decodeMap[str(i)] = 1
        for i in range(0, 7):                                                                                   #Decode "*x", 0 <= x <= 6.
            decodeMap["*" + str(i)] = 2
        for i in range(7, 10):                                                                                  #Decode "*x", 7 <= x <= 9.
            decodeMap["*" + str(i)] = 1
        last2, last1 = 1, decodeMap[s[0]]                                                                       #Initialize the ways to decode 2 letters before and 1 letter before.
        for i in range(1, len(s)):                                                                              #Traverse s from the 2nd letter.
            last2, last1 = last1, (last1 * decodeMap[s[i]] + last2 * decodeMap[s[i - 1:i + 1]]) % division      #Dynamically update last1 and last2.
        return last1                                                                                            #Return last1.
