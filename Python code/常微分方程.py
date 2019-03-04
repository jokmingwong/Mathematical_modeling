from sympy import sin, symbols, cos,integrate

x = symbols('x')
print(integrate(1 /(cos(x)**3 + sin(x)**3),x))

"""
c1 = 0.00048070
c2 = 0.30243
c7 = c3 = c2
c4 = 665.625
c5 = 95.898
c6 = 0.62956
# 下面简化常数项
a1 = float((c6 * c1 + c2 * c4) / (c1 * c4))
a2 = float(c2 * (c6 - c2) / (c1 * c4))
a3 = float((c2 * c5) / (c1 * c4))
T1 = Function('T1')

T2 = Function('T2')

t = Symbol('t')

t2 = Symbol('t2')

print(dsolve(diff(T2(t), t, 2) - a1 * diff(T2(t), t) - a2 * T2(t) - a3))
"""
