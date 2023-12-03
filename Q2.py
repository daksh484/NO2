def objective_fn(x):
    return x**2+4*x+4

def gradient(x):
   return 2*x+4

def line_search(initial_x,learning_rate,epsilon):
    x=initial_x
    iteration=0

    while True:
        gradient_x=gradient(x)
        new_x=x-learning_rate*gradient_x

        if abs(new_x-x)<epsilon:
            break

        x= new_x
        iteration+=1
    return x,objective_fn(x),iteration


initial_x=0.0
learning_rate=0.1   #step size
epsilon=1e-6       #stopping condition

result_x,result_min,iteration=line_search(initial_x,learning_rate , epsilon)


print(f"Minimum value found at x={result_x}")
print(f"Minimum objective function value ={result_min}")
print(f"Iteration={iteration}")
