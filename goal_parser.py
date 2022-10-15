
# category == string
from hashlib import new
import os
os.system('cls||clear')
# ========================= Function =====================
# SOLVED!


class Solution:
    def interpret(self, command):
        return command.replace("()", "o").replace("(al)", "al")


# ========================= Variables =====================
command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".
# Example 2:

command_1 = "G()()()()(al)"
# Output: "Gooooal"
# Example 3:

command_2 = "(al)G(al)()()G"
# Output: "alGalooG"

# ========================= Script =====================

s = Solution()
print(s.interpret(command_2))
