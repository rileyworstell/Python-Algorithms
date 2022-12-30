class Solution:
    def singleNumber(self, nums) -> int:
        # O(n) time, O(1) space
        # if you do XOR of two same bits, it returns 0
        # if you do XOR of zero and some bit, it will return that bit
        a = 0
        for i in nums:
            a ^= i
        return a

    def duplicateNumber(self, nums) -> int:
        # O(1) space, O(n) time
        # xor with 2 raised to the i and if that is less than a then that number is the duplicate
        a = 0
        for i in nums:
            newA = a ^ (2**i)
            if newA < a:
                return i
            else:
                a = newA


x = Solution()
print(x.singleNumber([4, 1, 2, 1, 2])) # 4
print(x.duplicateNumber([1, 2, 3, 4, 1])) # 1
