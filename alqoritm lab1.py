x = float(input("x:"))
epsilon = 0.01
term = 1
S = 0
n = 1
fakt=1
while abs(term)  > epsilon:
    print(term)
    S += term
    fakt=fakt*n
    term = ( x**n) / fakt
    n += 1

print("S:", S)