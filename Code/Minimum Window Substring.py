class Solution:
    # @return a string
    def minWindow(self, S, T):
        n=len(S)
        m=len(T)
        if n==0 or m==0:
            return ""
        dict={}                                             #Count the number of appearances of each character in T.
        for c in T:
            if not dict.has_key(c):
                dict[c]=1
            else:
                dict[c]+=1
        minLenth=n                                          #Minimum length of window is the length of S.
        result=""
        i=0
        appearance={}                                       #Count the current number of appearances of each character in T.
        for c in T:
            appearance[c]=0
        first=S[i]                                          #Record the beginning index of the window.
        index=[]                                            #Record the sequence of index of character.
        count=0                                             #Record the current number of appeared character.
        j=0
        while i<n:
            if S[i] not in T:
                i+=1
            else:
                first=S[i]                                  #Update first.
                if j<i:                                     #J should be greater than or equal to i.
                    j=i
                while j<n and count<m:
                    if appearance.has_key(S[j]):
                        index.append(j)                     #Append current index to index.
                        if appearance[S[j]]<dict[S[j]]:     #If current number of appearances of S[j] is smaller than the total number of appearances of S[j], we find a valid appearance of S[j], so update count.
                            count+=1
                        appearance[S[j]]+=1                 #Update appearance.
                    j+=1
                if count==m:                                #This means that a window is found.
                    while appearance[first]>dict[first]:    #Deal with the duplicate characters in the beginning of window.
                        appearance[first]-=1                #Update appearance.
                        index.remove(index[0])              #Remove index of duplicate characters.
                        first=S[index[0]]                   #Update the beginning character of window.
                        i=index[0]                          #Update the beginning index of window.
                    length=index[-1]-index[0]+1
                    if length<=minLenth:                    #If current window length is small than minLength, update minLength.
                        minLenth=length
                        result=S[index[0]:index[-1]+1]      #Update result.
                    
                if len(index)>1:                            #If the window has more than one characters in T.
                    index.remove(i)                         #Remove the index of beginning character of window.
                    appearance[S[i]]-=1                     #Update appearance.
                    i=index[0]                              #Update i and search for the window beginning with the second valid character of current window.
                    count-=1                                #Update count.
                else:                                       #If the window has more than one characters in T.
                    i=i+1
        return result                                       #Return result.
