import os
from re import X
import turtle
from unicodedata import name
os.system('cls||clear')


class Solution:

    def isPalindrome(self, x: int) -> bool:
        return (str(x)) == str(x)[::-1]
