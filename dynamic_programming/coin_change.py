# https://leetcode.com/problems/coin-change/


class Solution:
    # tabulation bottom - up
    # Time O(n*m) where n is length of coins and m is amount
    # Space O(m) where m is amount
    def coinChange(self, coins, amount: int) -> int:
        arr = [float('inf') for _ in range(amount+1)]
        arr[0] = 0
        for coin in coins:
            for i in range(1, len(arr)):
                if i >= coin and arr[i-coin] != float('inf'):
                    if arr[i] != 0:
                        arr[i] = min(1 + arr[i-coin], arr[i])
                    else:
                        arr[i] = (1 + arr[i-coin])
        if arr[-1] == float('inf'):
            return -1
        return arr[-1]



coins = [1, 2, 5]
amount = 11
x = Solution()
print(x.coinChange(coins, amount))
# 11 = 5 + 5 + 1
