# EVCS Placement Optimisation on Sioux Falls Network

This project formulates and solves an electric vehicle charging station (EVCS) placement optimisation problem using the **Sioux Falls transportation network**. The objective is to **minimise total operational cost** while ensuring all EV demand is met.

---

## 🧠 Problem Description

We model the network as a set of nodes and links. Each node may have a certain EV charging demand. The goal is to determine:
- Where to place charging stations (subject to a budget on number of stations),
- How to assign each node’s demand to installed stations,
- While minimising:
  - Fixed cost of installing stations,
  - Variable cost of serving demand (proportional to distance).

---

## 🧮 Optimisation Model

### Decision Variables
- `x[j] ∈ {0,1}`: whether to install a station at node `j`.
- `y[i,j] ≥ 0`: amount of demand from node `i` assigned to station at node `j`.

### Objective
Minimise total cost:
Total Cost = Σ (x[j] × station_cost) + Σ (y[i,j] × distance[i,j] × per_km_cost)

### Constraints
- Each node’s full demand must be met.
- Demand can only be assigned to nodes where a station is placed.
- Stations can only be assigned if within a given **coverage radius**.
- The number of stations is limited (`max_stations`).

---

## 📂 File Structure
📁 Aathirakdas01-RR_EVCS_optimisation/
│
├── Input/network.csv           # Link data with columns: from, to, distance, capacity
├── Input/ev_demand.csv         # EV demand at each node: node, demand
├── evcs_optimisation.py        # Main Python script
└── README.md                   # This file
