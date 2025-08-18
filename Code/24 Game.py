class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def evaluate(s: List) -> set():                                                                    #Evaluate all possible results of current formula with different ways to insert parentheses.
            if len(s) == 1:                                                                                #If s only has 1 element, return it in a set.
                return set([s[0]])
            result = set()                                                                                 #Initialize result set.
            for i in range(1, len(s) - 1, 2):                                                              #Visit each operator.
                r1, r2 = evaluate(s[:i]), evaluate(s[i + 1:])                                              #Dive s into 2 parts and evaluate each recursively to simulate parentheses over each part.
                for x, y in product(r1, r2):                                                               #Enumerate each result pair.
                    if s[i] == '/' and not y:                                                              #Cannot divide by 0 so move on.
                        continue
                    result.add(operators[s[i]](x, y))                                                      #Add evaluation result of the pair based on current operator, then add it to result set.
            return result
        
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}       #Store operations in a dictionary by the operator.
        cards_permutations = permutations(cards)                                                           #Generate permutaions of cards.
        for c in cards_permutations:                                                                       #Traverse each permutation.
            for x in operators.keys():                                                                     #Enumerate first operator.
                for y in operators.keys():                                                                 #Enumerate second operator.
                    for z in operators.keys():                                                             #Enumerate third operator.
                        s = evaluate([c[0], x, c[1], y, c[2], z, c[3]])                                    #Evaluate possible results of current formulat.
                        for r in s:                                                                        #Traverse possible results.
                            if abs(r - 24) <= 0.0001:                                                      #If current result is close enough to 24, return true.
                                return True
        return False                                                                                       #Return false at the end.
