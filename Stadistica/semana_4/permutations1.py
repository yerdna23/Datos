# modify this cell
import itertools as it
def compositions(k, n):
    # inputs: k and n are of type 'int'
    # output: a set of tuples
    a = set(range(n-1))
    total = len(set(it.combinations(a,k-1)))
    f = n-(k-1)
    d = [1]*(k-1) + [n-(k-1)]
    s = set({})
    a = set(it.permutations(d,k))
    s = s.union(a)
    u = 1
    v = 0
    l = 0
    h = 0
    while d[-1] != 0 and len(s) < total and u <= f - 1:
        for j in range(f-1):
            d[-1] = d[-1] - u
            d[l] = d[l] + u
            a = set(it.permutations(d,k))
            s = s.union(a)
            g =len(s)
            v = v + u
            l += 1
            if l > h:
                l = 0
            if v >= f - 1 or d[-1] - u <= 0:
                break
        v = 0
        h += 1
        d = [1]*(k-1) + [n-(k-1)]
        if h == k-1:
            d = [1]*(k-1) + [n-(k-1)]
            u += 1
            h = 0
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

