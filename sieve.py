# i - sieve
MX = 31622
pi = [0] * (MX + 1)
for i in range(2,MX + 1):
    if pi[i] == 0:
        pi[i] = pi[i-1] + 1
        for j in range(i*i, MX + 1, i):
            pi[j] = -1
    else:
        pi[i] = pi[i - 1]
