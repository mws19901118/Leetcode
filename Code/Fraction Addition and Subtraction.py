class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0].isdigit():                                          #Append a '+' if the expression starts with a digit.
            expression = '+' + expression
        fractions = defaultdict(int)                                         #Store the fractions in dictionary, key is denominator and value is numerator.
        index = 0
        while index < len(expression):                                       #Traverse expression.
            sign = 1 if expression[index] == '+' else -1                     #Get the sign of fraction.
            index += 1
            i = index                                                        #Get the absolute value of numerator.
            while i < len(expression) and expression[i].isdigit():
                i += 1
            numerator = int(expression[index:i]) * sign                      #Calculate the real value of numerator.
            index = i + 1
            i = index                                                        #Get the denominator.
            while i < len(expression) and expression[i].isdigit():
                i += 1
            denominator = int(expression[index:i])
            index = i
            fractions[denominator] += numerator                              #Add numerator to fractions[denominator].
        numerator, denominator = 0, 1                                        #Initialize result numerator and denominator to be 0 and 1.
        for k, v in fractions.items():                                       #Traverse fraction.
            if v:                                                            #If the current numerator is not 0, add current fraction to result.
                numerator = numerator * k + v * denominator                  #Calculate the new numerator.
                denominator *= k                                             #Calculate the new denominator.
        x = gcd(numerator, denominator)                                      #Calculate the gcd between numerator and denominator.
        return str(numerator // x) + "/" + str(denominator // x)             #Simplify the fraction and convert to string and return.
