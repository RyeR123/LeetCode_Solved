from enum import unique
import os
os.system('cls||clear')


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] == nums[j]:
                        nums[j] = "_"
        for i in range(len(nums)):
            if nums[i] == "_":
                nums.append(nums.pop(nums.index("_")))
        k = len(nums) - nums.count("_")
        return k


list_1 = [1, 1, 2]
list_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
list_3 = [-3, -1, -1, 0, 0, 0, 0, 0, 2]
list_4 = [0, 0, 0, 0, 0]

solution = Solution()
print(solution.removeDuplicates(list_4))
