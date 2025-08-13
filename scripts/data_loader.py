# -------------------------------
# Functions to load input data
# -------------------------------

import pandas as pd
from scripts import config  # import config from same package

def load_network_data():
    """Load the network data CSV as a pandas DataFrame."""
    return pd.read_csv(config.NETWORK_CSV_PATH)
1
def load_demand_data():
    """Load the EV demand data CSV as a pandas DataFrame."""
    return pd.read_csv(config.DEMAND_CSV_PATH)