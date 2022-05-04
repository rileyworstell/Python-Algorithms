# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
# O(nlogk) time # O(k) space
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heap = []
        for i in nums:
            if len(heap) < k:
                heapq.heappush(heap, i)
            else:
                heapq.heappushpop(heap, i)
        return heap[0]


x = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(x.findKthLargest(nums, k))
