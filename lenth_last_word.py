import os
os.system('cls||clear')


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[len(words) - 1])


s = "Hello World"
solution = Solution()
print(solution.lengthOfLastWord(s))
