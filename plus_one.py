class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        str_list = str(int("".join([str(nums) for nums in digits])) + 1)
        digits = [char for char in str_list]
        return digits


digits = [9]
solution = Solution()
print(solution.plusOne(digits))
