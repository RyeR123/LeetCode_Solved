class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums.sort()
        result = [i for i in range(
            1, len(nums) + 1) if i not in nums]
        return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]
solution = Solution()
print(solution.findDisappearedNumbers(nums))

# not solved
