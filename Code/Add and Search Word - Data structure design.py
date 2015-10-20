import re                                                             #Import regular expression.
class WordDictionary:
    
    def __init__(self):
        self.list=[]                                                  #Use list to store words.

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        if not word in self.list:                                     #If word is not in list, append it to list.
            self.list.append(word)

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        for i in self.list:
            if len(i)==len(word) and re.match(word,i):                #If there is an element in list which has the same length with word and match the regular expression of word, return true; otherwise, return false.
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
