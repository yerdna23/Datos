# modify this cell
import itertools as it
def compositions(k, n):
    # inputs: k and n are of type 'int'
    # output: a set of tuples
    A = set(range(n-1))
    total = len(set(it.combinations(A,k-1)))
    f = n-(k-1)
    d = [1]*(k-1) + [n-(k-1)]
    s = set({})
    a = set(it.permutations(d,k))
    s = s.union(a)
    u = 1
    v = 0
    l = 0
    while d[-1] != 0 and len(s) < total:
        h = f - u
        for j in range(f-2):
            if d[-1] - u < 1:
                break
            d[-1] = d[-1] - u
            d[l] = d[l] + u
            a = set(it.permutations(d,k))
            s = s.union(a)
            g =len(s)
            v = v + u
            l += 1
            if l == k-1:
                l = 0
            elif v >= f:
                break
        v = 0

        d = [1]*(k-1) + [n-(k-1)]
        u += 1
        if u > f  or len(s) > total:
            break
    print_compositions(s)

    return s, total, len(s)


    # YOUR CODE HERE
    #
def print_compositions(func_out):
    for x in func_out:
        string = ""
        for i in x:
            string = string + str(i)+ " + "
        print(string[0:-2])   
