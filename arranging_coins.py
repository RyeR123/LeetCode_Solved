class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 1
        while n > 0:
            rows += 1
            n -= rows
        return rows - 1


n = 8

solution = Solution()
print(solution.arrangeCoins(n))
