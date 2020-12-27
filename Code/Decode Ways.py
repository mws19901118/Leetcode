class Solution:
    def numDecodings(self, s: str) -> int:
        ways = [1]                                                              #Record the number of decode ways
        ways.append(0 if s[0] == "0" else 1)
        for i in range(1, len(s)):                                              #Scan from the second digit to the end.
            way = 0
            if s[i] != "0":                                                     #If current digit is not 0, add the ways count for string ended with previous digit to way.
                way += ways[-1]
            if int(s[i - 1:i + 1]) >= 10 and int(s[i - 1:i + 1]) <= 26:         #If current 2 digits is between 10 and 26, add the ways count for string ended with the digit 2 digits ahead. 
                way += ways[-2]
            ways.append(way)                                                    #Append way to the list.
        return ways[-1]                                                         #Return the last item of the list.
