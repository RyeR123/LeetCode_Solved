
# category == string
import os
os.system('cls||clear')
# ========================= Function =====================

# SOLVED!


class Solution:
    def finalValueAfterOperations(self, operations):
        total = 0
        for operation in operations:
            if "-" in operation:
                total -= 1
            elif "+" in operation:
                total += 1
        return total


# ========================= Variables =====================
operations_1 = ["--X", "X++", "X++"]
operations_2 = ["++X", "++X", "X++"]
operations_3 = ["X++", "++X", "--X", "X--"]

# ========================= Script =====================

s = Solution()
print(s.finalValueAfterOperations(operations_2))
