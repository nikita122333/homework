#дз 2.1
from pickle import DICT
e = '(()[][{()}])'
dict = {"(": ")", "[": "]", "{": "}"}
stack = []
f = 0
for c in e:
  if c in dict:
    stack.append(c)
  elif not stack or dict[stack.pop()] != c:
    f = 1

if f == 0:
  print('true')
else:
  print('false')



#дз 2.2
from collections import deque
first_list = deque([1,3,5,7])
second_list = deque([2,4,6,8])
list = zip(first_list, second_list)
print(sorted(deque(list)))