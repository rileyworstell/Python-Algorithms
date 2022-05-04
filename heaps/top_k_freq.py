# https://leetcode.com/problems/top-k-frequent-elements/

import heapq
# Time O(nlog(k)), if k < n
# Space O(n)
class Solution:
    def topKFrequent(self, nums, k):
        hashMap = {}
        for i in nums:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
            
        heap = []
        for key, value in hashMap.items():
            heapq.heappush(heap, (value * -1, key))
        
        ans = []
        for i in range(k):
            popped = heapq.heappop(heap)
            ans.append(popped[1])
        return ans



x = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2

print(x.topKFrequent(nums, k))
