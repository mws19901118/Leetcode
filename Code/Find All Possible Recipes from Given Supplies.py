class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adjacentList, inDegree = defaultdict(list), defaultdict(int)          #Build the adjacent list for each ingredient and indegree of each recipe.
        for recipe, ingredient in zip(recipes, ingredients):
            inDegree[recipe] = len(ingredient)
            for x in ingredient:
                adjacentList[x].append(recipe)
        result = []
        q = supplies
        while q:                                                              #Topological sort in BFS.
            newq = []
            for x in q:
                for y in adjacentList[x]:
                    inDegree[y] -= 1
                    if not inDegree[y]:
                        result.append(y)                                     #Append y to result if its degree is 0 meaning all ingredients are fulfilled.
                        newq.append(y)                                       #Also append it to newq, because now it can be used as ingredient of other recipe.
            q = newq
        return result
