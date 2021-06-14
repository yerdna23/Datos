#Generate the sum of k coin flips, repeat that n times
def generate_counts(k=1000,n=100):
    X = 2* (random.randint(k,n)> 0.5)- 1 #generate a kXn matrix of +-1 rando
    S = sum(X,axis=0)
    return S

