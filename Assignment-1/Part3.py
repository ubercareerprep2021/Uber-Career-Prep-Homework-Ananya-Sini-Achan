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
         self.values.insert(0, item)

    def pop(self):
         return self.items.pop()

    def top(self):
         return self.items[0]
    
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


class Queue(object):
    
    def __init__(self):
        self.values = []
        
    def enqueue(self, num):
        self.values.append(num)
        
    def dequeue(self):
        return self.values.pop(0)
    
    def rear(self):
        return self.values[-1]
    
    def front(self):
        return self.values[0]
    
    def size(self):
        return len(self.values)
    
    def isEmpty(self):
        return self.values == []


myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)

print("Size of queue: ", myQueue.size())
# prints “Size of queue: 3”

print("Front of queue: ", myQueue.front())
# prints “Front of queue: 1”

print("Rear of queue: ", myQueue.rear())
# prints “Rear of queue: 3”

dequeuedItem = myQueue.dequeue()
print("Dequeue item: ", dequeuedItem)
# prints “Dequeued item: 1”
