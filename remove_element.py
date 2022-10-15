import os
os.system('cls||clear')


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = len(nums)
        while val in nums:
            for i in range(len(nums)):
                if nums[i] == val:
                    nums[i] = "_"
                    nums.append(nums.pop(i))
                    k -= 1
        return k


nums_list2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
nums_list = [3, 2, 2, 3]
val = 3

solution = Solution()
print(solution.removeElement(nums_list2, val2))
