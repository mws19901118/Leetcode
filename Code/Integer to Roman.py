class Solution:
    def intToRoman(self, num: int) -> str:              #Use a table to store Roman numeral corresponding to each digit.
        table = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'], ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'], ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'], ['', 'M', 'MM', 'MMM']]
        roman = ''
        for i in reversed(range(4)):
            l = 10 ** i
            roman += table[i][num // l]                 #Convert the integer to Roman numeral digit by digit.
            num %= l
        return roman
