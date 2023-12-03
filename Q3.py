import sympy as sp
#define et
x1, x2 = sp.symbols('×1 x2')

function = 100* (x2 - x1**2)**2 + (1 - x1)*2
# Calculate the gradient
gradient = [sp.diff (function, x1), sp.diff(function, x2)]
# Calculate the Hessian matrix
hessian = [[sp.diff (gradient [0], x1), sp.diff(gradient [0], x2)],
[sp.diff (gradient [1], x1), sp.diff (gradient [1], x2)]]
# Print the gradient and Hessian
print("Gradient.")
print(gradient)
print ("InHessian:")
print (hessian)
