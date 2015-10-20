class TrieNode:
    # Initialize your data structure here.
    list=[]                                                             #Use list to store each character; its length is 26.
    hasValue=False                                                      #Indicate if there is a word ending here.
    def __init__(self):
        self.list=[None]*26
        self.hasValue=False
        

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        def insertInNode(word,index,root):
            c=ord(word[index])-97                                       #Map character to index.
            if root.list[c]==None:                                      #If current character is not in the list, add it to the list.
                root.list[c]=TrieNode()
            if index==len(word)-1:                                      #If the word ends, set the indicator to true.
                root.list[c].hasValue=True
            else:                                                       #If the word doesn't end, insert its next character recursively.
                insertInNode(word, index+1, root.list[c])
        
        if len(word)>0:
            insertInNode(word, 0, self.root)

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        def searchInNode(word,index,root):
            c=ord(word[index])-97                                       #Map character to index.
            if root.list[c]==None:                                      #If current character is not in the list, return false.
                return False
            else:
                if index==len(word)-1:                                  #If the word ends, return the indicator.
                    return root.list[c].hasValue
                else:
                    return searchInNode(word, index+1, root.list[c])    #If the word doesn't end, search its next character recursively.
        
        if len(word)>0:
            return searchInNode(word, 0, self.root)
        else:
            return True

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        def startsInNode(prefix,index,root):
            c=ord(prefix[index])-97                                     #Map character to index.
            if root.list[c]==None:                                      #If current character is not in the list, return false.
                return False
            else:
                if index==len(prefix)-1:                                #If the prefix ends, return true.
                    return True
                else:
                    return startsInNode(prefix, index+1, root.list[c])  #If the prefix ends, return true, search its next character recursively.

        if len(prefix)>0:
            return startsInNode(prefix, 0, self.root)
        else:
            return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
