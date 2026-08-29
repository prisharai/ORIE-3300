import cvxpy as cp

r = cp.Variable(nonneg=True, name="Regular") # hours regular 
p = cp.Variable(nonneg=True, name="Plus")  # hours plus 
u = cp.Variable(nonneg=True, name="Ultra") # hours ultra 

profit = (10000*(10/100))*r + (9000*(11/100))*p + (8500*(12/100))*u


constraints = []
constraints += [r + p + u == 24]
constraints += [10000*r <= 120000]
constraints += [9000*p <= 120000]
constraints += [8500*u <= 120000]

problem = cp.Problem(cp.Maximize(profit), constraints)

problem.solve(solver=cp.GUROBI, verbose=False)

print("objective = %s" % problem.value)

for variable in problem.variables():
    print("%s = %s" % (variable.name(), variable.value))

