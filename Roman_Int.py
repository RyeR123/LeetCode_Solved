import os
os.system('cls||clear')


class Solution:
    def __init__(self, s="") -> None:
        ...

    def romanToInt(self, s: str):
        roman = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9,
            "XL": 40, "XC": 90, "CD": 400, "CM": 900

        }

        input_list = []
        temp_list = []
        total = 0

        for i in range(len(s)):
            input_list.append(s[i])

        while len(input_list) > 1:
            temp_list.append(input_list[0])
            temp_list.append(input_list[1])
            y = ''.join(temp_list)
            temp_list.remove(input_list[0])
            temp_list.remove(input_list[1])
            if y in roman:
                total += roman[y]
                input_list.remove(input_list[0])
                input_list.remove(input_list[0])
            elif input_list[0] in roman:
                total += roman[input_list[0]]
                input_list.remove(input_list[0])
        if len(input_list) == 1:
            total += roman[input_list[0]]
            input_list.remove(input_list[0])

        return total


x = Solution()


print(x.romanToInt(s="MCMXCIV"))
