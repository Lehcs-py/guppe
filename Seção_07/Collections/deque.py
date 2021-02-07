from collections import deque

deq = deque('LEHCS')
print(deq)
deq.append('A')
print(deq)
deq.appendleft('D')
print(deq)

print(deq.pop())
print(deq)
print(deq.popleft())
print(deq)
