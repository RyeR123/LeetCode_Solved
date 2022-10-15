
import os
from collections import deque
os.system('cls||clear')

# Stack with lists
# s = []
# s.append("Url")
# s.append("Url/1")
# s.append("Url/2")
# s.append("Url/3")
# s.append("Url/4")


# print(s[-1])
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())

# stack with deque
stack = deque()
stack.append("Url")
stack.append("Url/1")
stack.append("Url/2")
stack.append("Url/3")
stack.append("Url/4")

# access and remove last element in stack
stack.pop()


print(stack)
