from itertools import product

def complement_of_union(A, B, U):
    # inputs: A, B and U are of type 'set'
    # output: a tuple of the type (set, set)
    
    '''(set, set, set)-> tuple of set

    The complement of union is a funtion with the set
    A, B and U retorn the complemet of union of set A
    and set B.
    
    A = {1, 2, 3}
    B = {3, -6, 2, 0}
    U = {-10, -9, -8, -7, -6, 0, 1, 2, 3, 4}
    >>> complement_of_union(A, B, U)
    ({-6, 0, 1, 2, 3}, {-10, -9, -8, -7, 4})
    '''
    C = A | B
    Ac = U - A
    Bc = U - B
    Cc = Ac & Bc
    R = (C,Cc)
    return R

def intersection_of_complements(A, B, U):
    # inputs: A, B and U are of type 'set'
    # output: a tuple of the form (set, set)

    '''(set, set, set) -> tuple of set

    The intersection of complemet is a funtion that return
    the intersection of complements of sets A anb B, use the
    universal complement U.
    
    A = {1, 2, 3}
    B = {3, -6, 2, 0}
    U = {-10, -9, -8, -7, -6, 0, 1, 2, 3, 4}
    >>> intersection_of_complements(A, B, U)
    ({-10, -9, -8, -7, -6, 0, 4}, {-10, -9, -8, -7, 4})
    '''
    Ac = U - A
    Bc = U - B
    Ic =Ac & Bc
    R = (Ac,Ic)
    return R

def product_of_unions(A, B, S, T):
    '''(set, set, set, set) -> tuples of tuples

    product_of_unions is a funtion that return of cartecian
    product of union of A and B with S and T.

    A = {1, 2}
    B = {1, 3}
    S = {-1, 0}
    T = {0, 10}
    >>> product_of_unions(A, B, S, T)
    ({1, 2, 3},
 {(1, -1),
  (1, 0),
  (1, 10),
  (2, -1),
  (2, 0),
  (2, 10),
  (3, -1),
  (3, 0),
  (3, 10)})
    '''
    AB = A | B
    ST = S | T
    Cart_AB_ST = set({})
    for i in product(AB,ST):
        Cart_AB_ST.add(i)
    R = (AB, Cart_AB_ST)
    return R

def union_of_products(A, B, S, T):
    # inputs: A, B, S and T are sets
    # output: a tuple of the type (set, set)
    '''(set, set, set, set) -> tuples of sets
    A = {1, 2}
    B = {1, 3}
    S = {-1, 0}
    T = {0, 10}
    >>> union_of_products(A, B, S, T)
    ({(1, -1), (1, 0), (2, -1), (2, 0)},
     {(1, -1),
      (1, 0),
      (1, 10),
      (2, -1),
      (2, 0),
      (2, 10),
      (3, -1),
      (3, 0),
      (3, 10)})
    '''
    Cart_A_S = set({})
    Cart_A_T = set({})
    Cart_B_S = set({})
    Cart_B_T = set({})
    for i in product(A,S):
        Cart_A_S.add(i)
    for i in product(A,T):
        Cart_A_T.add(i)
    for i in product(B,S):
        Cart_B_S.add(i)
    for i in product(B,T):
        Cart_B_T.add(i)
    R = (Cart_A_S , Cart_A_S | Cart_A_T | Cart_B_S | Cart_B_T)
    return R
