"""
https://leetcode.com/problems/process-restricted-friend-requests/
"""

class UF:
    def __init__(self, n):
        self.arr = [i for i in range(n)]

    def find(self, n):
        if self.arr[n] != n:
            self.arr[n] = self.find(self.arr[n])
        return self.arr[n]

    def union(self, a, b):
        a1 = self.find(a)
        b1 = self.find(b)
        self.arr[a1] = b1


class Solution:
    def friendRequests(self, n, restr, requests):
        uf = UF(n)
        ans = []
        for request in requests:
            toAdd = True
            x = uf.find(request[0])
            y = uf.find(request[1])

            for restriction in restr:
                a = uf.find(restriction[0])
                b = uf.find(restriction[1])
                if set([x, y]) == set([a, b]):
                    toAdd = False
                    break
            ans.append(toAdd)
            uf.union(x, y)
        return ans


n = 3
restrictions = [[0,1]]
requests = [[1,2],[0,2]]
x = Solution()
print(x.friendRequests(n, restrictions, requests))
