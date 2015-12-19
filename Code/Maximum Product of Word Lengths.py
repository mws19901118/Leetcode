class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dict = {}
        for s in words:
            integer = 0
            for c in s:
                integer |= 1 << (ord(c) - ord('a'))             #Map the letter set of a string to a 26-bit integer. Each bit indicates if the string has correspoding letter.
            if integer not in dict:
                dict[integer] = len(s)                          #Store the length of string in a dict and the key is the correspoding integer.
            else:
                dict[integer] = max(dict[integer], len(s))      #For every integer, only store the length of the longest string.
        result = 0
        for i in dict.keys():                                   #Traverse through every 2 integer pair.
            for j in dict.keys():
                if i & j == 0:                                  #If the and value of 2 integer is 0, the 2 strings don't share common letter.
                    result = max(result, dict[i] * dict[j])     #Update the max product.
        return result
