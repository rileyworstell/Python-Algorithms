# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
from collections import defaultdict

class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        # topological sort
        # the key here is the in_degree, this keeps track of
        # how many ingredients in a recipe
        graph = {}
        in_degree = defaultdict(int)
        for r,ing in zip(recipes,ingredients):
            for i in ing:
                if graph.get(i) != None:
                    graph[i].append(r)
                else:
                    graph[i] = [r]
                in_degree[r]+=1

        queue = supplies[::]
        res = []
        # pop off items from the queue, if the item is a recipe add to answer. Otherwise if that item is used to make something then reduce the count of that something and if that count is now 0 add it to the q.
        while queue:
            ing = queue.pop(0)
            if ing in recipes:
                res.append(ing)
            if graph.get(ing) != None:
                for child in graph[ing]:
                    in_degree[child]-=1
                    if in_degree[child]==0:
                        queue.append(child)

        return res


x = Solution()
recipes = ["bread","sandwich","burger"]
ingred = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
sup = ["yeast","flour","meat"]
print(x.findAllRecipes(recipes, ingred, sup))
