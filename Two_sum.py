class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and i > j:
                    if nums[i] + nums[j] == target:
                        return [j, i]


two = Solution()

print(two.twoSum([3, 3], 6))
