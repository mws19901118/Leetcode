class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for s in strs:
            t = ''.join(sorted(s))          #"Sort" the string. Group anagrams have the same sorted string.
            if t in dict:
                dict[t].append(s)
            else:
                dict[t] = [s]
        for x in dict.keys():               #Sort each inner list.
            dict[x].sort()
        return dict.values()
