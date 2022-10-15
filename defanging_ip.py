from audioop import add
import os
os.system('cls||clear')
# ========================= Function =====================


class Solution:
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")

# ========================= Variables =====================


address_1 = "255.100.50.0"
address_2 = "1.1.1.1"

# ========================= Script =====================

s = Solution()
print(s.defangIPaddr(address_1))
