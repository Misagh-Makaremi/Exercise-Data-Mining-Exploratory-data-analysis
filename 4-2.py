import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('C:/Users/ARTA PC/Desktop/Ex1-Misagh Makaremi/4-2-data.csv')  # Replace 'your_file.csv' with the actual file name

#4-2-a
print('#4-2-a:')

# Calculate mean, median, and standard deviation for age
mean_age = df['age'].mean()
median_age = df['age'].median()
std_dev_age = df['age'].std()

# Calculate mean, median, and standard deviation for fat
mean_fat = df['fat'].mean()
median_fat = df['fat'].median()
std_dev_fat = df['fat'].std()

# Print the results
print("Age - Mean:", mean_age, " Median:", median_age, " Standard Deviation:", std_dev_age)
print("fat - Mean:", mean_fat, " Median:", median_fat, " Standard Deviation:", std_dev_fat)

#4-2-b
print('4-2-b:')

import matplotlib.pyplot as plt

# Create a boxplot for age
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.boxplot(df['age'])
plt.title('Boxplot for Age')
plt.ylabel('Age')

# Create a boxplot for fat
plt.subplot(1, 2, 2)
plt.boxplot(df['fat'])
plt.title('Boxplot for fat')
plt.ylabel('fat')

# Show the plots
plt.show()

#4-2-c
print('4-2-c:')

import statsmodels.api as sm

# Scatter plot
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 2)
plt.scatter(df['age'], df['fat'])
plt.title('Scatter Plot')
plt.xlabel('Age')
plt.ylabel('fat')

# Q-Q plot
plt.subplot(1, 2, 2)
sm.qqplot(df['age'], line='s')  # Q-Q plot for 'age'
plt.title('Q-Q Plot for Age')

# Show the plots
plt.show()