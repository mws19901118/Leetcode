class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        for s in strs:
            l = len(s)
            result += str(l)                                #Put the length of each string with an additional space in front of each string as the delimiter.
            result += " "
            result += s
        return result
        
    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        result = []
        i = 0
        l = len(s)
        while i < l:
            j = i
            while j < l and s[j] != ' ':                    #Get the length of each string.
                j += 1
            t = int(s[i:j])
            j += 1                                          #Jump over the additional space.
            result.append(s[j:j + t])                       #Append the target string to result list according to its length.
            i = j + t
        return result

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
