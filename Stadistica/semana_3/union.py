def union(A, B):
    # inputs: A and B are of type 'set'
    # output: a tuple of the type (set, set_length)
    
    #
    '''(set, set) -> tuple(set, int)
        The function union return the union
        of A anb B without the size of the
        union.
    >>> A = {1, 2, 3}
    >>> B = {3, -6, 2, 0}
    >>> union(A, B)
    ({-6, 0, 1, 2, 3}, 5)
    '''
    C = A
    for i in B:
        if i not in A :
            C.add(i)
    R = (C, len(C))
    return R

def inclusion_exclusion(A, B):
    # inputs: A and B are of type 'set'
    # output: a tuple of four integers
    
    #
    A_l = len(A)
    B_l = len(B)
    S_A_B = A_l + B_l
    size = min(A_l,B_l)
    if size == A_l:
        C = A
        D = B
    else:
        C = B
        D = A
    i = 0
    inter = 0
    while i <= len(C) or C[i] in D:
        inter += 1
    exc = S_A_B - inter
    R =(A_l,B_l,inter,exc)
    return R
def union3(A, B, C):
    # inputs: A, B and C are of type 'set'
    # output: a tuple of the type (set, set_length)
    
    #
    '''
    >>> A = {1, 2, 3, 4, 5}
    >>> B = {0, 2, -6, 5, 8, 9}
    >>> C = {2, 10}
    >>> union3(A, B, C)
    >>> ({-6, 0, 1, 2, 3, 4, 5, 8, 9, 10}, 10)
    '''
    D = A
    O = (B, C)
    for i in O:
        for j in i:
            D.add(j)
    R = (D, len(D))
    return R
# modify this cell

def inclusion_exclusion3(A, B, C):
    # inputs: A, B and C are of type 'set'
    # output: a tuple of two integers
    
    #
    D = A
    O = (B, C)
    for i in O:
        for j in i:
            D.add(j)
    J = min(len(A),len(B),len(C))
    if J == len(A):
        J = A
        M = B
        N = C
    elif J == len(B):
        J = B
        M = A
        N = C
    elce:
        J = C
        M = A
        N = B
    for i in J:
        inter = 0
        if j in M and j in N:
            inter += 1
    R = (inter,len(D))
    return R
    #
