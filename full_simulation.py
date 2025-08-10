import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

# -----------------------------
# 1. Generate Customers
# -----------------------------
def generate_customers(n):
    names = ['Aanu', 'Tunde', 'Chioma', 'Bola', 'Emeka', 'Zainab', 'Ifeanyi', 'Ngozi']
    customers = []
    for i in range(n):
        customer = {
            'id': i + 1,
            'name': random.choice(names),
            'email': f'user{i+1}@example.com',
            'visits': random.randint(1, 5)
        }
        customers.append(customer)
    return customers

# -----------------------------
# 2. Simulate Queue
# -----------------------------
def simulate_queue(customers, arrival_rate=0.2, service_rate=0.3):
    n = len(customers)
    arrival_times = np.cumsum(np.random.exponential(1/arrival_rate, n))
    service_times = np.random.exponential(1/service_rate, n)
    start_times = np.zeros(n)
    wait_times = np.zeros(n)

    for i in range(n):
        if i == 0:
            start_times[i] = arrival_times[i]
        else:
            start_times[i] = max(arrival_times[i], start_times[i-1] + service_times[i-1])
        wait_times[i] = start_times[i] - arrival_times[i]
        customers[i]['arrival_time'] = round(arrival_times[i], 2)
        customers[i]['service_time'] = round(service_times[i], 2)
        customers[i]['start_time'] = round(start_times[i], 2)
        customers[i]['wait_time'] = round(wait_times[i], 2)

    return customers

# -----------------------------
# 3. Visualizations
# -----------------------------
def plot_customer_visits(customers):
    names = [c['name'] for c in customers]
    visits = [c['visits'] for c in customers]
    plt.figure(figsize=(12, 6))
    plt.bar(names, visits, color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.title('Customer Visit Counts')
    plt.xlabel('Customer Name')
    plt.ylabel('Number of Visits')
    plt.tight_layout()
    plt.savefig('customer_visits_bar_chart.png')
    plt.close()

def plot_wait_time_distribution(customers):
    wait_times = [c['wait_time'] for c in customers]
    plt.figure(figsize=(10, 6))
    sns.histplot(wait_times, bins=30, kde=True, color='teal')
    plt.title('Distribution of Wait Times')
    plt.xlabel('Wait Time (minutes)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('wait_times_histogram.png')
    plt.close()

def plot_customer_activity(customers):
    timestamps = pd.date_range(start='2025-01-01', periods=len(customers), freq='D')
    df = pd.DataFrame({
        'timestamp': timestamps,
        'visits': [c['visits'] for c in customers]
    })
    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df['visits'], marker='o', linestyle='-', color='green')
    plt.title('Customer Activity Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Visits')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('customer_activity_timeseries.png')
    plt.close()

# -----------------------------
# 4. Export CSV
# -----------------------------
def export_to_csv(customers, filename='customer_report.csv'):
    df = pd.DataFrame(customers)
    df.to_csv(filename, index=False)

# -----------------------------
# 5. Run Everything
# -----------------------------
if __name__ == '__main__':
    customers = generate_customers(100)
    customers = simulate_queue(customers)
    plot_customer_visits(customers)
    plot_wait_time_distribution(customers)
    plot_customer_activity(customers)
    export_to_csv(customers)
    print("✅ Simulation complete. Images and CSV saved.")
