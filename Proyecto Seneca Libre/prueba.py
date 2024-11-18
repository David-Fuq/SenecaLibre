import pyomo.environ as pyo
from pyomo.contrib.appsi.solvers import Highs

#Define the model
model = pyo.ConcreteModel()

#Define variables
model.x = pyo.Var(within=pyo.NonNegativeReals)
model.y = pyo.Var(within=pyo.NonNegativeReals)

#Define the objective function
model.obj = pyo.Objective(expr=2 * model.x + 3 * model.y, sense=pyo.maximize)

#Define constraints
model.con1 = pyo.Constraint(expr=3 * model.x + 4 * model.y <= 1)
model.con2 = pyo.Constraint(expr=2 * model.x + model.y <= 0.5)

#Create the HiGHS solver instance
solver = Highs()

#Solve the model
results = solver.solve(model)

#Display results
model.display()
