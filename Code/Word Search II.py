class Trie:                                                                               #Implement prefix tree class.
    list=[]
    hasValue=False
    def __init__(self):
        self.list=[None]*26
        self.hasValue=False
    
    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self,word,index):
        c=ord(word[index])-97
        if self.list[c]==None:
            self.list[c]=Trie()
        if index==len(word)-1:
            self.list[c].hasValue=True
        else:
            self.list[c].insert(word, index+1)
            
class Solution:
    def dfs(self,ans,trie,board,i,j,word):                                                  #Depth-first search
        if trie.hasValue:                                                                   #If current node of trie has a word, append it to the answer list and set the hasValue flag to false.
            ans.append(word)
            trie.hasValue=False
        if i>=0 and i<len(board) and j>=0 and j<len(board[0]) and board[i][j]!='#':         #Check if the coordinate of current position is out of bound and if current position has already been visited.
            char=board[i][j]                                                                #Record the character in current position.
            c=ord(char)-97                                                                  #Get its sequence number in alphabet.
            next=trie.list[c]                                                               #Get the object for current character in trie node.
            w=word+char                                                                     #Append current character to word.
            if next!=None:                                                                  #If the object is not none, trie node has at least a word begin with current word.
                board[i][j]='#'                                                             #Set current position as visited.
                self.dfs(ans,next,board,i+1,j,w)                                            #DFS in four directions.
                self.dfs(ans,next,board,i-1,j,w)
                self.dfs(ans,next,board,i,j+1,w)
                self.dfs(ans,next,board,i,j-1,w)
                board[i][j]=char                                                            #Restore the character in current position after DFS.
                
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        t=Trie()
        for i in words:
            t.insert(i,0)                                                                     #Insert word into trie.
        ans=[]
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                self.dfs(ans,t,board,i,j,'')                                                  #Do dfs at each position of the board.
        return ans
