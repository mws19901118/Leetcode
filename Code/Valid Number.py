class Solution:
    def isInteger(self, s: str) -> bool:                                                                                                                    #Check if s is integer.
        if s and s[0] in "+-":                                                                                                                              #Remove leading '+' or '-'.
            s = s[1:]
        return s.isdigit()                                                                                                                                  #Return if s only has digits.
    
    def isDecimal(self, s: str) -> bool:                                                                                                                    #Check if s is decimal.
        if s and s[0] in "+-":                                                                                                                              #Remove leading '+' or '-'.
            s = s[1:]
        splits = s.split('.')                                                                                                                               #Split by '.'.
        if len(splits) > 2:                                                                                                                                 #If there are more than 2 numbers in splits, return false.
            return False
        elif len(splits) == 2:                                                                                                                              #If there are 2 numbers in splits, they should both only has digits or one has digits and the other is one empty.
            return (splits[0].isdigit() and splits[1].isdigit()) or (not splits[0] and splits[1].isdigit()) or (splits[0].isdigit() and not splits[1])
        elif len(splits) == 1:                                                                                                                              #If there is 1 number in splits, it should only has digits.
            return s.isdigit()
        
    def isNumber(self, s: str) -> bool:
        splits = s.lower().split('e')                                                                                                                       #Convert s to lowercase and split by 'e'.
        return (self.isDecimal(splits[0]) or self.isInteger(splits[0])) and (len(splits) == 1 or (len(splits) == 2) and self.isInteger(splits[1]))          #The first number in splits must be either decimal or integer; if there is another number after 'e', it must be integer.
