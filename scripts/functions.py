
import pandas as pd
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, LpContinuous, PULP_CBC_CMD
from . import config

# -------------------------------
# Functions to load input data
# -------------------------------


def load_network_data():
    """Load the network data CSV as a pandas DataFrame."""
    return pd.read_csv(config.NETWORK_CSV_PATH)

def load_demand_data():
    """Load the EV demand data CSV as a pandas DataFrame."""
    return pd.read_csv(config.DEMAND_CSV_PATH)

# -------------------------------
# function for Core optimisation logic
# -------------------------------

def build_and_solve_model(node_list, demand_node, dist_matrix):
# Create a new linear programming problem to minimize operational cost
    
    model = LpProblem("EVCS_Operational_Cost_Minimisation", LpMinimize)

    # Define binary decision variables x[j] for whether to open a station at node j
    x = {j: LpVariable(f"x_{j}", cat=LpBinary) for j in node_list}

    # Define continuous decision variables y[i, j] for demand from node i assigned to station j
    # Only create y[i, j] if the distance between i and j is within coverage distance
    y = {
        (i, j): LpVariable(f"y_{i}_{j}", lowBound=0, cat=LpContinuous)
        for i in node_list for j in node_list
        if (i, j) in dist_matrix and dist_matrix[i, j] <= config.COVERAGE_DIST
    }
    
 # Set the objective function:
    # Total cost = sum of fixed costs for stations + sum of variable costs based on assigned demand and distance
    model += (
        lpSum(x[j] * config.FIXED_COST for j in node_list) +
        lpSum(y[i, j] * dist_matrix[i, j] * config.VARIABLE_COST for (i, j) in y)
    )
    
 # Constraint 1: Ensure all demand at each node i is fully assigned to some station j
    for i in node_list:
        model += lpSum(y[i, j] for j in node_list if (i, j) in y) == demand_node[i]

# Constraint 2: Cannot assign demand to a station j unless it is open
    for (i, j) in y:
        model += y[i, j] <= demand_node[i] * x[j]
        
# Constraint 3: Limit the total number of stations to MAX_STATIONS
    model += lpSum(x[j] for j in node_list) <= config.MAX_STATIONS

   # Solve the optimization problem using CBC solver 
    model.solve(PULP_CBC_CMD(msg=1))

    # Return the solved model and the decision variable dictionaries
    return model, x, y
