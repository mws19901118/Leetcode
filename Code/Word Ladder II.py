class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        def buildpath(traces,path,word):
            if len(traces[word])==0:
                path.append(word)
                currentpath=list(path)                      #Watch out, never ever shallow copy!
                currentpath.reverse()
                pathes.append(currentpath)
                path.pop()
                return 
            path.append(word)
            for i in traces[word]:
                buildpath(traces,path,i)
            path.pop()
        
        pathes=[]
        alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        dict.add(start)
        dict.add(end)
        length=len(start)
        traces={}
        for i in dict:
            traces[i]=[]
        a=set()
        b=set()
        layers=[a,b]
        cur=0
        pre=1
        layers[cur].add(start)
        while(True):
            cur=1-cur
            pre=1-pre
            for word in layers[pre]:
                dict.remove(word)
            layers[cur].clear()
            for word in layers[pre]:
                for i in range(length):
                    formerPart=word[:i]
                    latterPart=word[i+1:]
                    for j in alphabet:
                        if j!=word[i]:
                            next=formerPart+j+latterPart
                            if next in dict:
                                traces[next].append(word)
                                layers[cur].add(next)
            if len(layers[cur])==0:
                return pathes
                break
            if end in layers[cur]:
                break
            
        path=[]
        buildpath(traces,path,end)
        return pathes

        #说实话这道题我不会，照着别人C++代码改写的，然后陆牛帮我调了BUG，原博地址http://blog.csdn.net/niaokedaoren/article/details/8884938
