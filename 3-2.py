# Given data
intervals = [(1, 5), (6, 15), (16, 20), (21, 50), (51, 80), (81, 110)]
frequencies = [200, 450, 300, 1500, 700, 44]

# Calculate cumulative frequencies
cumulative_frequencies = [sum(frequencies[:i + 1]) for i in range(len(frequencies))]

# Find the median group
median_index = next(i for i, cf in enumerate(cumulative_frequencies) if cf >= sum(frequencies) / 2)
median_group = intervals[median_index]
lower_bound, upper_bound = median_group

# Calculate the approximate median
N = sum(frequencies)
F = cumulative_frequencies[median_index - 1] if median_index > 0 else 0
f = frequencies[median_index]
w = upper_bound - lower_bound

median = lower_bound + ((N / 2 - F) / f) * w

print("Approximate Median:", median)
