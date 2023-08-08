class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "".join(str(len(x)) + "#" + x for x in strs)            #Append length of each string and a delimiter '#' infront of each string as prefix and join them together.

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []                                                    #Initialize result.
        i = 0
        while i < len(s):                                              #Use 2 pointers to traverse s.
            j = i
            while j < len(s) and s[j].isnumeric():
                j += 1
            length = int(s[i:j])                                       #Get the length of current string.
            result.append(s[j + 1:j + 1 + length])                     #Extract the word and append it to result.
            i = j + 1 + length                                         #Move i to next string prefix.
        return result                                                  #Return result.


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
