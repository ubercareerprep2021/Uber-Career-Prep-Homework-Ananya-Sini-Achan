#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 18:26:12 2021

@author: Ananya
"""

def isStringPermutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

# Testing
print(isStringPermutation("asdf", "fsda") == True)
print(isStringPermutation("asdf", "fsa") == False)
print(isStringPermutation("asdf", "fsax") == False)


def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    pairs = []
    for i in range(len(inputArray)):
        for j in range(i, len(inputArray)):
            if ((inputArray[i] + inputArray[j]) ==  targetSum):
                pairs.append((inputArray[i],inputArray[j]))
    return pairs

# Testing
print(pairsThatEqualSum([1, 2, 3, 4, 5], 5) == [(1, 4), (2, 3)])
print(pairsThatEqualSum([1, 2, 3, 4, 5], 1) == [])
print(pairsThatEqualSum([1, 2, 3, 4, 5], 7) == [(2, 5), (3, 4)])
