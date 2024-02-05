from collections import deque

dq = deque([1, 2, 3, 3, 4, 2, 4])
dq.appendleft("name")
print(dq)
dq.popleft()
print(dq)