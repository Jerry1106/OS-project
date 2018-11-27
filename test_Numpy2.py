# +	np.add	Addition (e.g., 1 + 1 = 2)
# -	np.subtract	Subtraction (e.g., 3 - 2 = 1)
# -	np.negative	Unary negation (e.g., -2)
# *	np.multiply	Multiplication (e.g., 2 * 3 = 6)
# /	np.divide	Division (e.g., 3 / 2 = 1.5)
# //np.floor_divide	Floor division (e.g., 3 // 2 = 1)
# **np.power	Exponentiation (e.g., 2 ** 3 = 8)
# %	np.mod	Modulus/remainder (e.g., 9 % 4 = 1)
import numpy as np

x = np.array([-10, 1, 2, 0])
print(abs(x)) 
print('\n')

x = [1, 2, 3]
print("x", x)
print("e^x", np.exp(x)) 
print("2^x", np.exp2(x)) 
print("3^x", np.power(3, x))

#  A reduce repeatedly applies a given operation to the elements of an array until only a single result remains.
x = np.arange(1, 6)
print(x)
print(np.add.reduce(x))
print(np.multiply.reduce(x))
print(np.add.accumulate(x))
print(np.multiply.outer(x, x)


