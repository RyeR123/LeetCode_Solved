import os
os.system('cls||clear')


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]):
        result = []
        for number in nums1:
            if number in nums2:
                if number not in result:
                    result.append(number)
        return result


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

solution = Solution()
print(solution.intersection(nums1, nums2))
