#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 18:26:12 2021

@author: Ananya
"""
def isStringPermutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    
    if sum(map(ord,s1)) != sum(map(ord,s2)):
        return False
    
    character_count = {}
    for i in s1:
        if i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1
            
    for j in s2:
        if j in character_count:
            if character_count[j] == 1:
                del character_count[j] 
            else:
                character_count[j] -= 1
                
    if character_count == {}:
        return True
    
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
