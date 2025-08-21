# -------------------------------
# Constants and model settings
# -------------------------------

import os

# Absolute path to repo root (where scripts/ is located)
REPO_ROOT = os.path.dirname(os.path.dirname(__file__))

NETWORK_CSV_PATH = os.path.join(REPO_ROOT, "data", "network.csv")
DEMAND_CSV_PATH = os.path.join(REPO_ROOT, "data", "ev_demand.csv")
NETWORK_IMAGE_PATH = os.path.join(REPO_ROOT, "data", "Sioux-Falls-Network.jpg")

# Maximum distance covered
COVERAGE_DIST = 20

# Maximum number of stations allowed
MAX_STATIONS = 10

# Station installation cost
FIXED_COST = 1000

# Cost per unit demand per unit distance
VARIABLE_COST = 2