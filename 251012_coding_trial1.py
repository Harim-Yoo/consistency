from sympy import symbols, Eq, solve

a,b,c = symbols('a b c', real=True)

exp_1 = Eq(a**2 + 1, 3*b +c)
exp_2 = Eq (b**2 + 33, 7*c - 3*a)
exp_3 = Eq(c**2 - 5, b - 3*a)

solution = solve([exp_1,exp_2,exp_3], (a,b,c), dict=True)

print(solution)
