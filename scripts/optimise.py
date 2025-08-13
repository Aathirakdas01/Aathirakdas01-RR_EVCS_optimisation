# -------------------------------
# Core optimisation logic
# -------------------------------

from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, LpContinuous, PULP_CBC_CMD
from . import config

def build_and_solve_model(node_list, demand_node, dist_matrix):

    model = LpProblem("EVCS_Operational_Cost_Minimisation", LpMinimize)

    x = {j: LpVariable(f"x_{j}", cat=LpBinary) for j in node_list}
    y = {
        (i, j): LpVariable(f"y_{i}_{j}", lowBound=0, cat=LpContinuous)
        for i in node_list for j in node_list
        if (i, j) in dist_matrix and dist_matrix[i, j] <= config.COVERAGE_DIST
    }

    model += (
        lpSum(x[j] * config.FIXED_COST for j in node_list) +
        lpSum(y[i, j] * dist_matrix[i, j] * config.VARIABLE_COST for (i, j) in y)
    )

    for i in node_list:
        model += lpSum(y[i, j] for j in node_list if (i, j) in y) == demand_node[i]

    for (i, j) in y:
        model += y[i, j] <= demand_node[i] * x[j]

    model += lpSum(x[j] for j in node_list) <= config.MAX_STATIONS

    model.solve(PULP_CBC_CMD(msg=1))

    return model, x, y
