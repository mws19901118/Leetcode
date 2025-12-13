class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        validCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"                                                                                          #Initialize valid characters for coupon code.
        validCategory = ["electronics", "grocery", "pharmacy", "restaurant"]                                                                                                         #Initialize valid categories.
        return [y for _, y in sorted((b, c) for c, b, a in zip(code, businessLine, isActive) if a and b in validCategory and c and all(x in validCharacters for x in c))]            #Filter out valid coupon codes next sort by category then coupon code then return only the coupon code. 
