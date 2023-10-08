#solomon falode 2154980
# Read in coefficients of the first equation
a = int(input())
b = int(input())
c = int(input())

# Read in coefficients of the second equation
d = int(input())
e = int(input())
f = int(input())
# Brute force equation solver
solution_found = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and d * x + e * y == f:
            print(f"{x} {y}")
            solution_found = True
            break

if not solution_found:
    print("No solution")


