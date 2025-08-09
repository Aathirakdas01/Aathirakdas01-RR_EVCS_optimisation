# -------------------------------
# Core optimisation logic
# -------------------------------

from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, LpContinuous, PULP_CBC_CMD
from . import config

def build_and_solve_model(nodes, demand, dist_matrix):

    model = LpProblem("EVCS_Operational_Cost_Minimisation", LpMinimize)

    x = {j: LpVariable(f"x_{j}", cat=LpBinary) for j in nodes}
    y = {
        (i, j): LpVariable(f"y_{i}_{j}", lowBound=0, cat=LpContinuous)
        for i in nodes for j in nodes
        if (i, j) in dist_matrix and dist_matrix[i, j] <= config.COVERAGE_DIST
    }

    model += (
        lpSum(x[j] * config.FIXED_COST for j in nodes) +
        lpSum(y[i, j] * dist_matrix[i, j] * config.VARIABLE_COST for (i, j) in y)
    )

    for i in nodes:
        model += lpSum(y[i, j] for j in nodes if (i, j) in y) == demand[i]

    for (i, j) in y:
        model += y[i, j] <= demand[i] * x[j]

    model += lpSum(x[j] for j in nodes) <= config.MAX_STATIONS

    model.solve(PULP_CBC_CMD(msg=1))

    return model, x, y
