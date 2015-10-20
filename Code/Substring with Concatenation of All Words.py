class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        n=len(words)                                  #Record the number of words.
        m=len(words[0])                               #Record the length of each word.
        l=len(s)                                      #Record the length of string s.
        result=[]
        dict={}                                       #Count the appeareance of each word in words.
        for w in words:
            if dict.has_key(w):
                dict[w]+=1
            else:
                dict[w]=1
        for i in range(l-n*m+1):                      #Traverse every character from s[0] to s[l-m*n](the last possible beginning) as the beginning of concatenation of words.
            currentdict={}                            #Count current appeareance of each word in the window beginning with current i.
            j=0                                       #Record the number of matched words.
            while j<n:
                w=s[i+j*m:i+(j+1)*m]                  #Get the current word.
                if w not in words:
                    break
                if currentdict.has_key(w):
                    currentdict[w]+=1
                else:
                    currentdict[w]=1
                if currentdict[w]>dict[w]:            #If w appears more than the times appearing in words, break.
                    break
                j+=1
            if j==n:                                  #If find a exact concatenation, append i to result.
                result.append(i)
        return result
