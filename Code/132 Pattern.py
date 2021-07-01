#In Approach 2, we found out nums[i] corresponding to a particular nums[j] directly without having to consider every pair possible in numsnums to find this nums[i], nums[j] pair.
#If we do some preprocessing, we can make the process of finding a nums[k] corresponding to this nums[i],nums[j] pair also easy.
#
#The preprocessing required is to just find the best nums[i] value corresponding to every nums[j] value.
#This is done in the same manner as in the second approach i.e. we find the minimum element found till the j-th element which acts as the nums[i] for the current nums[j].
#We maintain thes values in a minmin array. Thus, min[j] now refers to the best nums[i] value for a particular nums[j].
#
#Now, we traverse back from the end of the numsnums array to find the nums[k]'s.
#Suppose, we keep a track of the nums[k] values which can potentially satisfy the 132 criteria for the current nums[j].
#We know, one of the conditions to be satisfied by such a nums[k] is that it must be greater than nums[i].
#Or in other words, we can also say that it must be greater than min[j] for a particular nums[j] chosen.
#
#Once it is ensured that the elements left for competing for the nums[k] are all greater than min[j](or nums[i]), our only task is to ensure that it should be lesser than nums[j].
#Now, the best element from among the competitors, for satisfying this condition will be the minimum one from out of these elements.
#
#If this element, nums[min] satisfies nums[min] < nums[j], we've found a 132 pattern.
#If not, no other element will satisfy this criteria, since they are all greater than or equal to nums[min] and thus greater than or equal to nums[j] as well.
#
#To keep a track of these potential nums[k] values for a particular nums[i],nums[j] considered currently, we maintain a stack on which these potential nums[k]'s satisfying the 132 criteria lie in a descending order(minimum element on the top).
#We need not sort these elements on the stack, but they'll be sorted automatically as we'll discuss along with the process.
#
#After creating a minmin array, we start traversing the nums[j] array in a backward manner.
#Let's say, we are currently at the j-th element and let's also assume that the stack is sorted right now.
#Now, firstly, we check if nums[j] > min[j]. If not, we continue with the (j−1)-th element and the stack remains sorted. If not, we keep on popping the elements from the top of the stack till we find an element, stack[top] such that, stack[top] > min[j](or stack[top] > nums[i]).
#
#Once the popping is done, we're sure that all the elements pending on the stack are greater than nums[i] and are thus, the potential candidates for nums[k] satisfying the 132 criteria.
#We can also note that the elements which have been popped from the stack, all satisfy stack[top] ≤ min[j].
#
#Since, in the min array, min[p] ≤ min[q], for every p > q, these popped elements also satisfy stack[top] ≤ min[k], for all 0 ≤ k < j.
#Thus, they are not the potential nums[k] candidates for even the preceding elements. Even after doing the popping, the stack remains sorted.
#
#After the popping is done, we've got the minimum element from amongst all the potential nums[k]'s on the top of the stack(as per the assumption).
#We can check if it is less than or equal to nums[j] to satisfy the 132 criteria(we've already checked stack[top] > nums[i]).
#If this element satisfies the 132 criteria, we can return a True value. If not, we know that for the current j, nums[j] > min[j].
#Thus, the element nums[j] could be a potential nums[k] value, for the preceding nums[i]'s.
#
#Thus, we push it over the stack.
#We can note that, we need to push this element nums[j] on the stack only when it didn't satisfy stack[top] < nums[j].
#Thus, nums[j] ≤ stack[top].
#Thus, even after pushing this element on the stack, the stack remains sorted.
#Thus, we've seen by induction, that the stack always remains sorted.
#
#Also, note that in case nums[j] ≤ min[j], we don't push nums[j] onto the stack.
#This is because this nums[j] isn't greater than even the minimum element lying towards its left and thus can't act as nums[k] in the future.
#
#If no element is found satisfying the 132 criteria till reaching the first element, we return a False value.

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, minValue = [], [nums[0]]
        for i in range(1, len(nums)):
            minValue.append(min(minValue[-1], nums[i]))
        for j in reversed(range(len(nums))):
            if nums[j] > minValue[j]:
                while stack and stack[-1] <= minValue[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False
