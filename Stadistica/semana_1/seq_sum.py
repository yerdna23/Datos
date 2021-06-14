import random
def seq_sum(n):
    m = []
    for i in range(n):
         k = random.randint(0,1)
         m.append(k)
    S = sum(m)
    return S,m

def estimate_prob(n,k1,k2,m):
    a = 0
    for i in range(m):
        [s, v] = seq_sum(n)
        if k1 <= s and s < k2:
            a =+1
    p = a/m
    return p
    

    
