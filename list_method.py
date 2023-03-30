list_methods = dir([])
for method in list_methods:
    if method.startswith ("__"):
        continue
    print(method)

a = [1, 2, 3]
a.append(7)
a.append('james')
print(a)
# a.clear()
# print(a)
b = a.copy()
a = [1, 1, 1, 1, 2, 2, 2, 1, 1]
print(a.count(1))

a = ['bob', 'james', 'jane']
print(a.index('jane'))
e = a.pop()
print(e, a)

import random
a = []
for i in range(100):
    a.append(random.randint(1, 1000))
print(a)
a.sort(reverse=True)
print(a)