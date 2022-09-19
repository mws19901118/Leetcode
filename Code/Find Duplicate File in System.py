class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        pathByContent = defaultdict(list)                                       #Store file path by content.
        for p in paths:                                                         #Traverse paths.
            segments = p.split(" ")                                             #Split p by " ".
            for x in segments[1:]:                                              #Traverse the rest segments.
                leftP = x.index('(')                                            #Find the index of left parentheses.
                fileName, content = x[:leftP], x[leftP + 1:-1]                  #Get the file name(before parenteses) and content(in parentheses).
                pathByContent[content].append(segments[0] + "/" + fileName)     #Concatenate directory and filename to get file path then hash it by file content.
        return [p for p in pathByContent.values() if len(p) > 1]                #Return all file paths list whose length is greater than 1.
