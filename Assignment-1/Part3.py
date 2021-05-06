#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 18:26:12 2021

@author: Ananya
"""

class Stack:
    def __init__(self):
         self.items = []

    def push(self, item):
         self.items.append(item)

    def pop(self):
         return self.items.pop()

    def top(self):
         return self.items[len(self.items)-1]
    
    def isEmpty(self):
         return self.items == []

    def size(self):
         return len(self.items)


myStack = Stack()
myStack.push(42)

print("Top of stack: ", myStack.top())
# prints “Top of stack: 42”

print("Size of stack: ", myStack.size())
# prints “Size of stack: 1”

popped_value = myStack.pop()
print("Popped value: " , popped_value)
# prints “Popped value: 42”

print("Size of stack: ", myStack.size())
# prints “Size of stack: 0”
