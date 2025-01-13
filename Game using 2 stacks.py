#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#USN:1BM23AIO27
#SECTION:3A

def twoStacks(maxSum, a, b):
    count = 0
    sum_a = 0
    
    for i in range(len(a)):
        if sum_a + a[i] > maxSum:
            break
        sum_a += a[i]
        count += 1

    max_count = count

    sum_b = 0
    for j in range(len(b)):
        sum_b += b[j]

        while sum_a + sum_b > maxSum and count > 0:
            sum_a -= a[count - 1]
            count -= 1

        if sum_a + sum_b <= maxSum:
            max_count = max(max_count, count + j + 1)

    return max_count

g = int(input().strip())

for temp in range(g):
    n, m, maxSum = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = twoStacks(maxSum, a, b)
    print(result)

