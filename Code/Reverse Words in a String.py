class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        result=''
        length=len(s)
        if length==0:
            return result
        last=length-1										#'last' point to the rear of the string
        while s[last]==' ' and last>=0:
            last=last-1
        if(last==-1):
            return result;
        while last>=0:
            if s[last]!=' ':						#find a word
                temp=last
                while s[temp]!=' ' and temp>=0:
                    temp=temp-1
                result=result+s[temp+1:last+1]			#add the 'word' to the result
                last=temp
            else:
                temp=last
                while s[temp]==' ' and temp>=0:			#deal with space(maybe more than one)
                    temp=temp-1
                if temp>=0:
                    result=result+' '
                    last=temp
                else:
                    last=temp
        return result
