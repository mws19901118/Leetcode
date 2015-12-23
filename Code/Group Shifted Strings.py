class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dict = {}                                                                                 #Use a dict to group all the shifted strings.
        for s in strings:
            flag = False                                                                          #Indicates if current string can be shifted to strings already in dict.
            for key in dict.keys():                                                               #Compare current string with each key in dict.
                if len(s) == len(key):                                                            #If one string can be shifted to another string, they should have the same length.
                    i = 0
                    while i < len(s):
                        if (ord(s[i]) - ord(key[i])) % 26 != (ord(s[0]) - ord(key[0])) % 26:      #If find a place where the distance between 2 characters is different with the distance of the first characters of 2 string, they can't be grouped together.
                            break
                        i += 1
                    if i == len(s):                                                               #If current string can be grouped to a key string, append it to the corresponding list, set flag to be true and break.
                        dict[key].append(s)
                        flag = True
                        break
            if flag is False:                                                                     #If current string can't be grouped to any key strings, set it as a new key.
                dict[s] = [s]
        result = dict.values()
        for l in result:
            l.sort()                                                                              #Sort every list.
        return result
