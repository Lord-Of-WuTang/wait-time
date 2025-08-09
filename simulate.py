import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🎲 Step 1: Simulate Wait Time Data
np.random.seed(42)
num_customers = 100
arrival_rate = 0.2  # customers per minute
service_rate = 0.3  # services per minute

# Generate inter-arrival and service times
inter_arrival_times = np.random.exponential(1/arrival_rate, num_customers)
service_times = np.random.exponential(1/service_rate, num_customers)

# Calculate arrival, service start, and departure times
arrival_times = np.cumsum(inter_arrival_times)
start_service = np.maximum.accumulate(arrival_times)
departure_times = start_service + service_times
wait_times = start_service - arrival_times

# Create DataFrame
df = pd.DataFrame({
    'Customer': range(1, num_customers + 1),
    'Arrival': arrival_times,
    'Service Start': start_service,
    'Departure': departure_times,
    'Wait Time': wait_times,
    'Service Time': service_times
})

# 📊 Step 2: Visualizations

# 1️⃣ Histogram of Wait Times
plt.figure(figsize=(10, 6))
sns.histplot(df['Wait Time'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Wait Times')
plt.xlabel('Wait Time (minutes)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 2️⃣ Scatter Plot: Arrival vs. Wait Time
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Arrival', y='Wait Time', data=df, color='orange')
plt.title('Arrival Time vs. Wait Time')
plt.xlabel('Arrival Time (minutes)')
plt.ylabel('Wait Time (minutes)')
plt.grid(True)
plt.show()

# 3️⃣ Bar Chart: Wait Time Ranges
bins = pd.cut(df['Wait Time'], bins=5)
wait_time_counts = bins.value_counts().sort_index()

plt.figure(figsize=(10, 6))
wait_time_counts.plot(kind='bar', color='mediumseagreen')
plt.title('Wait Time Ranges')
plt.xlabel('Wait Time Range (minutes)')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# 📈 Step 3: Summary Statistics
print("📌 Summary Statistics")
print(f"Average Wait Time: {df['Wait Time'].mean():.2f} minutes")
print(f"Max Wait Time: {df['Wait Time'].max():.2f} minutes")
print(f"Min Wait Time: {df['Wait Time'].min():.2f} minutes")
print(f"Standard Deviation of Wait Time: {df['Wait Time'].std():.2f} minutes")
