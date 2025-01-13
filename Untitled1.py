#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#USN:1BM23AIO27
#SECTION:3A

def isBalanced(s):
    brackets = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for i in s:
        if i in brackets:
            stack.append(i)
        else:
            if not stack:
                return "NO"
            top = stack.pop()
            if brackets[top] != i:
                return "NO"
    
    if stack:
        return "NO"
    
    return "YES"

n=int(input())
for i in range(n):
    s=input()
    print(isBalanced(s))

