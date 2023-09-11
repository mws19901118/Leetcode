class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        peopleByGroupSize = defaultdict(list)                        #Store people id whose group size is same in a list as value and group size as key.
        for i, x in enumerate(groupSizes):
            peopleByGroupSize[x].append(i)
        result = []
        for size, people in peopleByGroupSize.items():              #Traverse group size and its people ids.
            for i in range(len(people) // size):                    #Split people ids into groups that have required group size and append them to result.
                result.append(people[i * size:(i + 1) * size])
        return result
