import numpy as np #for python 2.7
np.random.seed(1)  # seed for reproducibility

x1 = np.random.randint(100, size=8)  # One-dimensional array
x2 = np.random.randint(20, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array
print(x1, x1[0], x1[2], x1[-2], x1[-1])
print(x2)
print(x3)
print('\n')

print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)

x1[0] = 2000
print(x1)
print('\n')

# x[start:stop:step]
x = np.arange(20)
print(x[:5])
print(x[5:])
print(x[5::])
print(x[::5])
print(x[4:8])
print(x[:7:3])
print(x[::-1])  # when the step value is negative. In this case, the defaults for start and stop are swapped
print('\n')

print(x2)
print(x2[:2, :3])
print(x2[:3, ::2])
print('\n')

# Reshaping of Arrays
Array = np.arange(15).reshape((3, 5))
print(Array)
print('\n')

# Concatenate, Vstack, Hstack
grid = np.array([[1, 2, 3], [4, 5, 6]])
print(np.concatenate([grid, grid]))
print(grid + grid)
print('\n')

grid2 = np.array([10, 11, 12])
print(np.vstack([grid, grid2]))
print('\n')

#Split arrays
x = np.arange(20)
a, b, c = np.split(x, [5, 19])
print(a, b, c)

