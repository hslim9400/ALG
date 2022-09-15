target = set(list(range(2, 10**6 + 1)))
for i in range(2, 1001):
    q = (10**6) // i
    for x in range(2, q+1):
        target.discard(i*x)
print(*target)