

from collections import deque

N = int(input())

operation = []
d = deque()
for i in range(N):
    operation = input().split()
    
    if operation[0] == 'append':
        d.append(operation[1])
    
    if operation[0] == 'appendleft':
        d.appendleft(operation[1])
        
    if operation[0] == 'pop':
        d.pop()
        
    if operation[0] == 'popleft':
        d.popleft()
        
li_d = list(d)
print(*li_d, sep=' ')