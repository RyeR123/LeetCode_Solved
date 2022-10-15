import os
os.system('cls||clear')


# class Solution:
#     def generate(self, numRows: int):
#         nums_list = [1]
#         if numRows == 1:
#             return numRows
#         if numRows > 1:
#             num_list = [[1, i]for i in range(1, numRows)]
#             num_list.insert(0, [1])

#             for i in range(len(num_list)):
#                 if i > 2:
#                     num_list[i].append(num_list[i][0] + num_list[i - 1][1])
#                     num_list[i].append(1)
#             return num_list

class Solution:
    def generate(self, numRows: int):
        res = [[1], ]

        for _ in range(numRows-1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res


n = 5
solution = Solution()
print(solution.generate(n))
