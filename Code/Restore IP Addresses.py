class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        for i in range(1, len(s)):                                                                                              #Enumerate the place to insert first delimiter.
            for j in range(i + 1, len(s)):                                                                                      #Enumerate the place to insert second delimiter.
                for k in range(j + 1, len(s)):                                                                                  #Enumerate the place to insert third delimiter.
                    if all(x and (x == "0" or (int(x) < 256 and x[0] != "0")) for x in [s[:i], s[i:j], s[j:k], s[k:]]):         #Check all 4 chunks are valid: not empty, between 0 to 255 and no leading 0.
                        result.append(".".join([s[:i], s[i:j], s[j:k], s[k:]]))                                                 #Join the chucks together with "." and add to result.
        return result
