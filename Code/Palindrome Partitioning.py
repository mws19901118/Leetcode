class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):                                       #The same method as Word Break II
        def Palindrome(s,dict):
            if s in dict:
                return True
            l=len(s)
            i=l/2-1
            while i>=0:
                if s[i]!=s[l-1-i]:
                    break
                i-=1
            if i==-1:
                dict.add(s)
                return True
            else:
                return False

        dict=set(['a'])  
        n=len(s)
        A=[None]*n
        i=n-1
    
        while i>=0:
            if Palindrome(s[i:n],dict):
                A[i]=[n]
            else:
                A[i]=[]
            for j in xrange(i+1,n):
                if A[j] and Palindrome(s[i:j],dict):
                    A[i].append(j)
            i-=1
            
        result=[]
        path_list=[[0]]
        while path_list:
            new_list=[]
            for path in path_list:
                if path[-1]==n:
                    temp=[ s[path[i]:path[i+1]] for i in xrange(len(path)-1) ]
                    result.append(temp)
                else:
                    for j in A[path[-1]]:
                        new_list.append(path+[j])
            path_list=new_list
        return result
