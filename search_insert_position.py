import os
os.system('cls||clear')


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


nums_list = [1, 3, 5, 6]
target = 7
solution = Solution()
print(solution.searchInsert(nums_list, target=target))
