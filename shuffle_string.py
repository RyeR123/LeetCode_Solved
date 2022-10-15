
# category == string
from hashlib import new
import os
os.system('cls||clear')
# ========================= Function =====================


class Solution:
    def restoreString(self, s, indices):
        new_word = {}
        for i in range(len(indices)):
            new_word[indices[i]] = s[i]

        compile = [new_word[i] for i in range(len(indices))]
        return "".join(compile)


# ========================= Variables =====================
s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
# Output: "leetcode"

# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
# Example 2:

s_1 = "abc"
indices_1 = [0, 1, 2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.

# ========================= Script =====================

solution = Solution()
print(solution.restoreString(s, indices))
