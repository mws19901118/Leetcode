class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        s.reverse()                                 #Reverse the whole list.
        l = len(s)
        if l == 0:
            return
        c = 0
        while c < l:                                #Traverse from start to end.
            t = 0
            while c + t < l and s[c + t] != ' ':    #Find every word.
                t += 1
            i = 0
            while i < t / 2:                        #Reverse it in-place.
                temp = s[c + t - 1 - i]
                s[c + t - 1 - i] = s[c + i]
                s[c + i] = temp
                i += 1
            c += t + 1
