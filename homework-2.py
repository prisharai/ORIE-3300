import cvxpy as cp
import numpy as np

y = cp.Variable(9) #y1, y2, ..., y9

x = cp.Variable((9, 9), boolean=True) # x[i,j]

constraints = []

for i in range(9): #property 1
    constraints += [cp.sum(x[i, :]) == 1]

for j in range(9): #property 2
    constraints += [cp.sum(x[:, j]) == 1]

values = np.arange(1, 10)

for i in range(9): #property 3
    constraints += [y[i] == values @ x[i, :]]

#rows
constraints += [y[0] + y[1] + y[2] == 15]
constraints += [y[3] + y[4] + y[5] == 15]
constraints += [y[6] + y[7] + y[8] == 15]
#columns
constraints += [y[0] + y[3] + y[6] == 15]
constraints += [y[1] + y[4] + y[7] == 15]
constraints += [y[2] + y[5] + y[8] == 15]
#diagonals
constraints += [y[0] + y[4] + y[8] == 15]
constraints += [y[2] + y[4] + y[6] == 15]

problem = cp.Problem(cp.Maximize(y[4]), constraints)
problem.solve(solver=cp.GUROBI)
print("Maximum y5 =", y[4].value)
print("y =", y.value)

problem = cp.Problem(cp.Minimize(y[4]), constraints)
problem.solve(solver=cp.GUROBI)
print("Minimum y5 =", y[4].value)
print("y =", y.value)


