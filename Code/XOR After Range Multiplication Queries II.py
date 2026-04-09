class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        division = 10 ** 9 + 7                                                            #Initialize division.
        n = len(nums)                                                                     #Get the length of nums.
        root = floor(sqrt(n))                                                             #Calculate the floor of square root of n.
        groups = [[] for _ in range(root)]                                                #Initialize groups as a list that contains root empty lists.
        for l, r, k, v in queries:                                                        #Traverse queries.
            if k < root:                                                                  #If k < root, append the query (l, r, v) to the group of k.
                groups[k].append((l, r, v))
            else:                                                                         #Otherwise, directly apply the operation of current query as it will only affect at most (n // root + 2) numbers.
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % division

        impact = [1] * (n + root)                                                         #Initialize the impact list, impact[i] means the multiplier to nums[i] after applying all operations in current query group. Add root virtual multipliers at the end.
        for k in range(1, root):                                                          #Enumerate all the k values.
            if not groups[k]:                                                             #If current group is empty, skip.
                continue
            impact = [1] * len(impact)                                                    #Reset impact.
            for l, r, v in groups[k]:                                                     #Traverse each query in current group.
                impact[l] = impact[l] * v % division                                      #Multiply impact[l] by v as l is the start. 
                end = ((r - l) // k + 1) * k + l                                          #Calculate the end index, which is the first index beyond r when traversing from l and moving k indexes each step.
                impact[end] = impact[end] * pow(v, division - 2, division) % division     #End is where the current query impact should end, so multiply impact[end] by the modular inverse of v under division 10 ** 9 + 7. This is according to Fermat's Little Theorem. 

            for i in range(k, n):                                                         #Traverse from k to n to populate impact[i] from impact[i - k].
                impact[i] = impact[i] * impact[i - k] % division
            for i in range(n):                                                            #Traverse nums to apply impact of current goup.
                nums[i] = nums[i] * impact[i] % division

        return reduce(lambda x, y: x ^ y, nums)                                           #Calculate the XOR result and return.
