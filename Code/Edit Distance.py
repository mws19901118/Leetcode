class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        m=len(word1)
        n=len(word2)
        if n==0 and m==0:
            return 0
        distance=[[0 for i in range(m+1)] for j in range(n+1) ]           #Distance[i][j] is the edit distance of the first i characters of word1 and the first j characters of word2.
        for i in range(n+1):
            for j in range(m+1):
                if i==0 and j!=0:                                         #If i is 0, we have to insert j character to make them same, so distance[0][j] is j.
                    distance[i][j]=j
                elif i!=0 and j==0:                                       #If j is 0, we have to insert i character to make them same, so distance[i][0] is i.
                    distance[i][j]=i
                elif i>=1 and j>=1:
                    cost=1
                    if word2[i-1]==word1[j-1]:                            #If the characters are same, cost of edit is 0; otherwise cost is 1.
                        cost=0
                    distance[i][j]=min(distance[i-1][j]+1,distance[i][j-1]+1,distance[i-1][j-1]+cost)     #Distance[i][j] is the min value of distance[i-1][j]+1(delete word1[i]), distance[i][j-1]+1(delete word2[j]), distance[i-1][j-1]+cost(replace word1[i] with word2[j]).
        return distance[n][m]                                             #Return the final edit distance.
