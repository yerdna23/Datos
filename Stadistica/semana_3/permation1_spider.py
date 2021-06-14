# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:36:36 2019

@author: Usuario
"""

# modify this cell
import itertools as it
def compositions(k, n):
    # inputs: k and n are of type 'int'
    # output: a set of tuples
    A = set(range(n-1))
    total = len(set(it.combinations(A,k-1)))
    d = [1]*(k-1) + [n-(k-1)]
    s = set({})
    a = set(it.permutations(d,k))
    s = s.union(a)
    for j in range(1,k):
        if d[-1] -1 < d[1] + 1:
            break
        for v in range(n-(k-1)-j+1):
            if d[-1] -1 < d[-(1 + j)] + 1:
                break
            d[-(1-v)] = d[-1] - 1
            d[-(1+j)] = d[-(1+j)] + 1
            a = set(it.permutations(d,k))
            s = s.union(a)
    print_compositions(s)
    return s, total
    # YOUR CODE HERE
    #
def print_compositions(func_out):
    for x in func_out:
        string = ""
        for i in x:
            string = string + str(i)+ " + "
        print(string[0:-2]) 

compositions(3, 6)