class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)            #Count each type of sandwich preference in students.
        for x in sandwiches:                 #Traverse sandwiches.
            if not count[x]:                 #If no one wants current sandwich, return the number of remain students prefering the other type.
                return count[1 - x]
            count[x] -= 1                    #Hand out current sandwich to a student.
        return 0                             #Return 0 at the end if all sandwiches are handed out.
