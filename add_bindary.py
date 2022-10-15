import os
os.system('cls||clear')


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), "b")


a = "11"
b = "1"

solution = Solution()
print(solution.addBinary(a, b))
