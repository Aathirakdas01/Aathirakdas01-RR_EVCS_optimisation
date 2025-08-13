# Tutorial Answers

## Structure

1. **Create seperate folders for scripts (including config.py, _init_.py, and functions) and Output**

   RR_EVCS_optimisation/
   --scripts/
      -- _init_.py
      -- config.py
      -- data_loader.py
      -- function.py
   --Output
   --notebooks
      --evcs_optimisation.ipynb

2. **Create `config.py`:**
   - Instead of hardcoding values, define constants in the file. Example:
     ```python
     COVERAGE_DIST = 20
     MAX_STATIONS = 10
     FIXED_COST = 1000
     VARIABLE_COST = 2
     ```
   - Define file paths
   ```python
     NETWORK_CSV_PATH = "data/network.csv"
     DEMAND_CSV_PATH = "data/ev_demand.csv"
     ```

3. **Create `_init_.py`:**
   - Include all  Imports and Configurations here
   ```python
     import os
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   from PIL import Image
   from pulp import (
   LpProblem, LpMinimize, LpVariable, lpSum,
   LpBinary, LpContinuous, PULP_CBC_CMD
   )

   from . import config
   from . import data_loader
   from . import optimise
     ```

 ## Functions

1. **Create `data_loader.py`:**
   - Define 'load_network_data()' and 'load_demand_data()' used to load input data.

2. **Add General `build_and_solve_model()` Function to `funcctions.py`:**
   - Also the function should have better names, include descritpions and have type annotations.
     ```python
        def build_and_solve_model(node_list, demand_node, dist_matrix):
            """
            Perform network optimisation.
            """
     ```

## Commenting/Segmentation/Naming

1. **Use Type Hints - Add Type Annotations to All Function Definitions:**
   - Add type annotations to function signatures for better clarity:

2. **Make Docstring Descriptions of Functions:**
   - Document each function with a concise description of its purpose, parameters, and return values:

3. **Use Section Headers to Separate Logical Blocks:**
   - Organize the code with section headers to improve readability and structure:
     ```python
      # ---------------------------------------------
      # Part 2: Load data and display network
      # ---------------------------------------------
      
      # -------------------------------
      # Part 3: Process data
      # -------------------------------
     ```


4. **Add Comments to Explain Non-Obvious Steps:**
   - Comment complex or non-intuitive logic, especially around window creation and indexing:
     ```python
     # Demand per node (ensure 0 demand for missing)
     ```

5. **Avoid Abbreviated Variable Names:**
   - Replace abbreviated variable names like `nodes`and `demand`  with more descriptive names such as `node_list`, and `demand_node`.

6. **PEP8 Formatting:**
   - Ensure the code adheres to PEP8 standards, with proper indentation, spacing, and line lengths.
