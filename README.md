# Queue Simulation Analysis

A comprehensive customer wait time simulation system for single-server queue analysis using exponential distributions and Nigerian customer data.

## Overview

This is a project that simulates realistic customer service scenarios by modeling queue behavior with exponentially distributed arrival and service times. The simulation generates detail analytics on customer wait times, service patterns, and queue performance metrics.

## feature

### Core Simulation Engine
- **Queue Modeling**: Single-server queue system with exponential arrival and service distributions
- **Customer Generation**: Realistic Nigerian customer profiles with visit history tracking
- **Wait Time Analysis**: Comprehensive calculation of wait times, service start times, and departure times
- **Performance Metrics**: Statistical analysis including mean, maximum, minimum, and standard deviation

### Data Management
- **Customer Profiles**: Generated customers include ID, name, email, and visit count
- **Comprehensive Tracking**: Records arrival times, service times, start times, and wait times
- **CSV Export**: Detailed customer reports exported to CSV format for further analysis
- **Sample Size**: Configurable customer count (default: 100 customers)

### Visualization Suite
- **Wait Time Distribution**: Histogram with kernel density estimation showing wait time patterns
- **Customer Activity Timeline**: Time series analysis of customer visit patterns over time
- **Visit Count Analysis**: Bar chart showing customer engagement levels
- **Interactive Plots**: All visualizations saved as PNG files for reporting

## Technical Specifications

### Simulation Parameters
- **Arrival Rate**: 0.2 customers/minute (5-minute average intervals)
- **Service Rate**: 0.3 services/minute (3.33-minute average service time)
- **Distribution Model**: Exponential distributions for both arrivals and service times
- ** Using a FIFO Model**
- **Customer Pool**: 8 Nigerian names (Tunde, Chioma, Bola, Emeka, Zainab, Ifeanyi, Ngozi)

### Queue Mechanics
- First-come, first-served (FCFS) scheduling
- Single server with no parallel processing
- Customers wait if server is busy
- Service begins immediately if server is available

## Installation

### Requirements
```
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0
```

### Setup
```bash
pip install numpy pandas matplotlib seaborn
```

## Usage

### Basic Simulation
```bash
python full_simulation.py
```

### Expected Output
The simulation generates:
- `customer_report.csv` - Detailed customer data and metrics
- `wait_times_histogram.png` - Wait time distribution visualization
- `customer_activity_timeseries.png` - Customer activity over time
- `customer_visits_bar_chart.png` - Visit frequency analysis
- Console summary with key statistics

### Sample Output Data
```csv
id,name,email,visits,arrival_time,service_time,start_time,wait_time
1,Ifeanyi,user1@example.com,5,13.08,2.46,13.08,0.0
2,Ngozi,user2@example.com,3,18.99,2.61,18.99,0.0
...
```

## Analysis Insights

### Queue Performance Patterns
- **Early Arrivals**: Customers arriving early typically experience zero wait time
- **Peak Periods**: Wait times increase during high-arrival periods (customers 40-60)
- **Maximum Wait**: Can reach up to 30 minutes during congestion
- **Distribution**: Most customers (60%+) experience minimal wait times

### Customer Behavior
- **Visit Frequency**: Random distribution between 1-5 visits per customer
- **Service Variation**: Service times vary exponentially (0.03 to 18.74 minutes observed)
- **Congestion Points**: Queue buildup typically occurs in middle simulation periods

## Future Enhancements

The simulation framework is designed for expansion:
- **Multi-server Systems**: Extend to parallel service channels
- **Priority Queues**: Implement customer priority levels
- **Real-time Data**: Integration with live customer arrival data
- **Advanced Analytics**: Predictive modeling and optimization algorithms
- **Interactive Dashboard**: Web-based visualization and control interface

## Data Structure

### Customer Object
```python
{
    'id': int,           # Unique customer identifier
    'name': str,         # Customer name from Nigerian pool
    'email': str,        # Generated email address
    'visits': int,       # Number of previous visits (1-5)
    'arrival_time': float,    # When customer arrives (minutes)
    'service_time': float,    # How long service takes (minutes)
    'start_time': float,      # When service actually begins (minutes)
    'wait_time': float        # Time spent waiting (minutes)
}
```

## Performance Notes

- **Scalability**: Current implementation handles 100-1000 customers efficiently
- **Memory Usage**: Minimal memory footprint with in-memory processing
- **Processing Time**: Sub-second execution for standard simulations
- **Output Files**: Generated visualizations are production-ready

## Contributing

This simulation provides a foundation for queue theory research and practical applications in service optimization. Extensions and improvements are welcome, particularly in areas of multi-server modeling and real-world validation.

---


*Note: This simulation uses exponential distributions which are standard in queueing theory but may need adjustment for specific real-world scenarios. Consider validating parameters against actual service data for production use.*



