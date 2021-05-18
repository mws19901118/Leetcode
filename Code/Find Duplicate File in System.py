class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        pathByContent = defaultdict(list)                                       #Store file path by content.
        for p in paths:                                                         #Traverse paths.
            segments = p.split(" ")                                             #Split p by " ".
            directory = segments[0]                                             #The first segment is directory.
            for s in segments[1:]:                                              #Traverse the rest segments.
                splits = s.split("(")
                fileName = splits[0]                                            #File name is before bracket.
                content = splits[1][:-1]                                        #Content is inside bracket.
                pathByContent[content].append(directory + "/" + fileName)       #Concatenate directory and filename to get file path then hash it by file content.
        return [p for p in pathByContent.values() if len(p) > 1]                #Return all file paths list whose length is greater than 1.
