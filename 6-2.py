import math

#6-2-a
print('#6-2-a:')

# Given tuples representing two objects
object1 = (22, 1, 42, 10)
object2 = (20, 0, 36, 8)

# Compute Euclidean distance
distance = math.sqrt(sum((x - y)**2 for x, y in zip(object1, object2)))

# Print the result
print("Euclidean Distance:", distance)

#6-2-b
print('6-2-b:')

# Given tuples representing two objects
object1 = (22, 1, 42, 10)
object2 = (20, 0, 36, 8)

# Compute Manhattan distance
manhattan_distance = sum(abs(x - y) for x, y in zip(object1, object2))

# Print the result
print("Manhattan Distance:", manhattan_distance)

#6-2-c
print('#6-2-c:')

# Given tuples representing two objects
object1 = (22, 1, 42, 10)
object2 = (20, 0, 36, 8)

# Set the value of q
q = 3

# Compute Minkowski distance
minkowski_distance = sum(abs(x - y)**q for x, y in zip(object1, object2))**(1/q)

# Print the result
print(f"Minkowski Distance with q={q}:", minkowski_distance)
