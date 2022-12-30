# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        courseMap = {}
        for i in prerequisites:
            if courseMap.get(i[0]) == None:
                courseMap[i[0]] = [i[1]]
            else:
                courseMap[i[0]].append(i[1])
            if courseMap.get(i[1]) == None:
                courseMap[i[1]] = []
        courses = []
        for key, value in courseMap.items():
            courses.append([key, value])
        # courses.sort(key= lambda x: len(x[1]))
        return self.dfs(numCourses, prerequisites, courseMap, courses[0][0])

    def dfs(self, numCourses, prerequisites, courseMap, cur, visited=set(), cameFrom={}):
        visited.add(cur)
        if  courseMap.get(cur) == []:
            return True
        else:
            for i in courseMap.get(cur):
                if cameFrom.get(cur) == i:
                    return False
                cameFrom[cur] = i
                canTake = self.dfs(numCourses, prerequisites, courseMap, i, visited, cameFrom)
                if canTake == False:
                    return False
        return True
        


# n = 5
# preReqs = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
n = 2
preReqs = [[0, 1], [1, 0]]
x = Solution()
print(x.canFinish(n, preReqs))
