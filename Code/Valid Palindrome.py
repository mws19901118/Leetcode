class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        def hw(dict,word):                #chech if palindrome
            if word in dict:
                return true
            length=len(word)
            i=0
            while i<length/2:
                if word[i]!=word[length-1-i]:
                    break
                i+=1
            if i==length/2:
                dict.add(word)
                return True
            else:
                return False
        
        dict=set()
        r=''
        l=len(s)
        for i in range(0,l):
            if ord(s[i])>=65 and ord(s[i])<=90:
                r+=chr(ord(s[i])+32)
            elif (ord(s[i])>=97 and ord(s[i])<=122) or (ord(s[i])>=48 and ord(s[i])<=57):
                r+=s[i]
        return hw(dict,r)
