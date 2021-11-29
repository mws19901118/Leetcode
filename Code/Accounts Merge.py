class UnionFind:                                                                    #Union find.
    def __init__(self, index: int):
        self.parent = self
        self.index = index
        
    def find(self) -> Optional['UnionFind']:
        if self.parent == self:
            return self
        self.parent = self.parent.find()
        return self.parent
    
    def union(self, uf) -> None:
        uf.find().parent = self.find()
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailMap = {}                                                               #Map each email to union find of its account.
        unionFinds = []                                                             #Initialize union find for each account.
        for i, account in enumerate(accounts):                                      #Traverse accounts.
            unionFinds.append(UnionFind(i))                                         #Create new union find with current index and append it to unionFinds.
            for email in account[1:]:                                               #Traverse emails of current account.
                if email not in emailMap:                                           #If email not in emailMap, set its value to the union find of current account.
                    emailMap[email] = unionFinds[-1]
                else:                                                               #Otherwise, union the union find of current account and the union find of the existing account of that email.
                    unionFinds[-1].union(emailMap[email])
        emailSetOfIndex = defaultdict(set)                                          #Create a map from the set of email to index.
        for uf in unionFinds:                                                       #Traverse unionFinds.
            emailSetOfIndex[uf.find().index].update(accounts[uf.index][1:])         #Add all emails of current account to the email set of the account which is the parent of current union find.
        return [[accounts[i][0]] + sorted(x) for i, x in emailSetOfIndex.items()]   #Traverse key-value paires in emailSetOfIndex and generate merged account in required format.
