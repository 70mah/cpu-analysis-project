import pandas as pd

# ============================================
# CPU Data Analysis Project
# ============================================

# File path for your data
file_path = '/storage/emulated/0/Download/Python_project/ec2_cpu_utilization.csv'

# Read the CSV file
data = pd.read_csv(file_path)

# ============================================
# Part 1: Basic Information
# ============================================
print("=" * 50)
print("CPU DATA ANALYSIS REPORT")
print("=" * 50)

print("\nTotal Rows:", len(data))
print("Total Columns:", len(data.columns))
print("Column Names:", list(data.columns))

# ============================================
# Part 2: Show First 5 Rows
# ============================================
print("\n" + "-" * 50)
print("First 5 Rows:")
print("-" * 50)
print(data.head())

# ============================================
# Part 3: Important Statistics
# ============================================
print("\n" + "=" * 50)
print("STATISTICS")
print("=" * 50)

print("\nMean:", round(data['value'].mean(), 4))
print("Max:", round(data['value'].max(), 4))
print("Min:", round(data['value'].min(), 4))
print("Std Deviation:", round(data['value'].std(), 4))

# ============================================
# Part 4: Anomaly Detection
# ============================================
print("\n" + "=" * 50)
print("ANOMALY DETECTION")
print("=" * 50)

# Calculate threshold (Mean + 2 * Std Deviation)
mean_val = data['value'].mean()
std_val = data['value'].std()
threshold = mean_val + 2 * std_val

print("\nThreshold:", round(threshold, 4))

# Find values greater than threshold
anomalies = data[data['value'] > threshold]

print("Number of Anomalies:", len(anomalies))
print("Percentage of Anomalies:", round((len(anomalies) / len(data)) * 100, 2), "%")

if len(anomalies) > 0:
    print("\nTop 5 Anomalies:")
    print(anomalies.head())

# ============================================
# End
# ============================================
print("\n" + "=" * 50)
print("✅ ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 50)