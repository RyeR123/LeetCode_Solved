
# category == string
import os
os.system('cls||clear')
# ========================= Function =====================
# SOLVED!


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str):
        jewel = [letter for letter in jewels]
        stone = [letter for letter in stones]

        total = 0
        for match in jewel:
            if match in stone:
                total += stone.count(match)
        return total


# ========================= Variables =====================
jewels = "aA"
stones = "aAAbbbb"
# Output: 3
# Example 2:

jewels_1 = "z"
stones_1 = "ZZ"
# Output: 0

# ========================= Script =====================

s = Solution()
print(s.numJewelsInStones(jewels, stones))
