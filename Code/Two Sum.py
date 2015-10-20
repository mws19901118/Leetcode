class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict={}
        for i in range(0,len(num)):                                         #construct dictionary
            if not dict.has_key(num[i]):
                dict[num[i]]=[i]
            else:
                dict[num[i]].append(i)
        for i in range(0,len(num)):
            if dict.has_key(target-num[i]):
                temp=dict[target-num[i]][0]                                 #temp is the index
                if temp==i:                                                 #in case of two equal items
                    if(len(dict[target-num[i]])>1):
                        return (i+1,dict[target-num[i]][1]+1)
                elif i<temp:
                    return (i+1,temp+1)
                else:
                    return (temp+1,i+1)
