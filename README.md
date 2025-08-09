# Queue Simulation Analysis

Simulates customer wait times in a single-server queue system using exponential distributions.

## What it does
- Generates 100 customers with random arrival and service times
- Calculates wait times, service start times, and departures
- Creates three visualizations:
  - Wait time distribution histogram
  - Arrival time vs wait time scatter plot
  - Wait time ranges bar chart
- Displays summary statistics (mean, max, min, std dev)

## Parameters
- **Arrival rate**: 0.2 customers/minute (5-minute average intervals)
- **Service rate**: 0.3 services/minute (3.33-minute average service)
- **Sample size**: 100 customers

## Requirements
```
numpy
pandas
matplotlib
seaborn
```

## Usage
```bash
python queue_simulation.py
```

## Output
- Interactive plots showing wait time patterns
- Console summary with key statistics

We obviously need a wider dataset to work with.
