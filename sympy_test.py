from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x')
#equation = input('Enter the expression to graph')
#expr = sympify(equation)
expr = 'exp(-abs(x))*sin(2*pi*x)**2'
f = lambdify(x, expr, "numpy")
a = np.linspace(-5, 5, 512)
res = f(a)

plt.plot(a, res)
plt.show()
