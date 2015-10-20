class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):                            #The main idea is to divide 4 integers into 2 group which has 2 integers and to use hash map to store the sum of every group.
        nums.sort()                                             #Sort the list.
        vdict={}                                                #Keys are the sum of each 2 elements and values are the index tuples of them.
        result=[]
        for i in range(len(nums)-1):                            #Put the indexes of 2 elements in a list as a tuple according to their sum.
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] not in vdict:
                    vdict[nums[i]+nums[j]]=[(i,j)]
                else:
                    vdict[nums[i]+nums[j]].append((i,j))
        value=vdict.keys()                                      #Get the total possible values of sum of 2 elements.
        for v in value:                                         #Traverse the values of sum.
            if v==target-v and len(vdict[v])>1:                 #If v equals target/2 and there are more than 1 tuples in vdict[v], there might be possible solutions.
                l=vdict[v]
                for t1 in range(len(l)-1):                      #Enumerate every combination of 2 tuples in vdict[v] which makes a group of 4 index of integers.
                    for t2 in range(t1+1,len(l)):
                        if l[t1][0]!=l[t2][0] and l[t1][0]!=l[t2][1] and l[t1][1]!=l[t2][0] and l[t1][1]!=l[t2][1]:         #Check if there are duplicate indexes.
                            temp=[nums[l[t1][0]], nums[l[t1][1]], nums[l[t2][0]], nums[l[t2][1]]]
                            temp.sort()                         #Sort the 4 integers corresponding to 4 indexes.
                            if temp not in result:              #If there are no duplicates in result, append the current list of 4 integers into result.
                                result.append(temp)
            elif v!=target-v and target-v in vdict:             #If v does not equal target/2 and target-v is in vdict, there might be possible solutions.
                l1=vdict[v]
                l2=vdict[target-v]
                for t1 in range(len(l1)):                       #Enumerate every combination of 2 tuples, one belongs to vdict[v] and one belongs to vdict[target-v], which makes a group of 4 index of integers.
                    for t2 in range(len(l2)):
                        if l1[t1][0]!=l2[t2][0] and l1[t1][0]!=l2[t2][1] and l1[t1][1]!=l2[t2][0] and l1[t1][1]!=l2[t2][1]: #Check if there are duplicate indexes.
                            temp=[nums[l1[t1][0]], nums[l1[t1][1]], nums[l2[t2][0]], nums[l2[t2][1]]]
                            temp.sort()                         #Sort the 4 integers corresponding to 4 indexes.
                            if temp not in result:              #If there are no duplicates in result, append the current list of 4 integers into result.
                                result.append(temp)
        return result
