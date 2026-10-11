import csv
import statistics
import numpy as np

#2-2-a
print('#2-2-a:')
# Replace 'your_data_file.csv' with the actual file path
file_path = 'C:/Users/ARTA PC/Desktop/Ex1-Misagh Makaremi/2-2-data.csv'

# Assuming the 'age' column is in the first column (index 0)
ages = []

with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row if it exists
    next(csv_reader, None)

    # Extract 'age' values from the CSV file
    for row in csv_reader:
        age = int(row[0])  # Assuming age is in the first column
        ages.append(age)

# Calculate mean and median
mean_age = statistics.mean(ages)
median_age = np.median(ages)

print(f"Mean Age: {mean_age}")
print(f"Median Age: {median_age}")

#2-2-b
print('#2-2-b:')

# Calculate mode
try:
    mode_age = statistics.mode(ages)
    print(f"Mode Age: {mode_age}")

except statistics.StatisticsError:
    print("There is no unique mode. The data is multimodal.")

#2-2-c
print('#2-2-c:')

# Calculate midrange
min_age = min(ages)
max_age = max(ages)
midrange_age = (min_age + max_age) / 2

print(f"Midrange Age: {midrange_age}")

#2-2-d
print('#2-2-d:')

# Calculate first quartile (Q1) and third quartile (Q3)
q1_age = np.percentile(ages, 25)
q3_age = np.percentile(ages, 75)

print(f"First Quartile (Q1): {q1_age}")
print(f"Third Quartile (Q3): {q3_age}")

#2-2-e
print('#2-2-e:')

# Calculate the five-number summary
minimum_age = np.min(ages)
q1_age = np.percentile(ages, 25)
median_age = np.median(ages)
q3_age = np.percentile(ages, 75)
maximum_age = np.max(ages)

print(f"Minimum: {minimum_age}")
print(f"First Quartile (Q1): {q1_age}")
print(f"Median: {median_age}")
print(f"Third Quartile (Q3): {q3_age}")
print(f"Maximum: {maximum_age}")

#2-2-f
print('#2-2-f:')

import matplotlib.pyplot as plt

# Create a boxplot
plt.boxplot(ages, vert=False)
plt.title('Boxplot of Age Data')
plt.xlabel('Age')
plt.show()
