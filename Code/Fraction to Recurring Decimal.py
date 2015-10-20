class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        ans=''
        if numerator*denominator<0:                                 #Deal with negative numbers.
            numerator=abs(numerator)
            denominator=abs(denominator)
            ans='-'
        if numerator%denominator==0:                                #Numerator can be divided with no remainder.
            ans=ans+str(numerator/denominator)    
        else:
            ans=ans+str(numerator/denominator)   
            remainder=numerator%denominator
            r={}                                                    #This is the dictionary, of which the key is already existing remainder and the value is its index.
            n=[]                                                    #This is the list recording the new numerator in sequence.
            index=0
            while remainder!=0 and r.has_key(remainder)==False:     #If current numerator can be divided with no remainder or we detect the recurring period, break.
                r[remainder]=index
                n.append(str(remainder*10/denominator))             #Long division method
                remainder=remainder*10%denominator
                index=index+1
            if remainder==0:
                ans=ans+'.'+''.join(n)                              #Join the list.
            elif r.has_key(remainder):
                ans=ans+'.'+''.join(n[:r[remainder]])+'('+''.join(n[r[remainder]:])+')'     #Join the list in two parts.
        return ans
