
# category == string
import os
os.system('cls||clear')
# ========================= Function =====================

# SOLVED!


class Solution:
    def mostWordsFound(self, sentences):
        max = 0
        for sentence in sentences:
            if len(sentence.split()) > max:
                max = len(sentence.split())
        return max


# ========================= Variables =====================

# Example 1:
sentences = ["alice and bob love leetcode",
             "i think so too", "this is great thanks very much"]
# Output: 6
# Explanation:
# - The first sentence, "alice and bob love leetcode", has 5 words in total.
# - The second sentence, "i think so too", has 4 words in total.
# - The third sentence, "this is great thanks very much", has 6 words in total.
# Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
# Example 2:

sentences_2 = ["please wait", "continue to fight", "continue to win"]
# Output: 3
# Explanation: It is possible that multiple sentences contain the same number of words.
# In this example, the second and third sentences (underlined) have the same number of words.

# ========================= Script =====================

s = Solution()
print(s.mostWordsFound(sentences_2))
