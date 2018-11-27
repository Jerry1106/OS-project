
import pandas as pd
import numpy as np

rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0, 10, 4)) #randint(>, <, num)
print(ser)

df = pd.DataFrame(rng.randint(0, 10, (4, 5)), columns = ['A', 'B', 'C', 'D', 'E'])
print(df)

print(np.exp(df))
print()

age1 = pd.Series([20, 21, 40, 25])
age2 = pd.Series([20, 21, 40, 25], index = list('abcd'))
age3 = pd.Series({'Jerry': 20, "Natalie": 21, "John": 40, "Panda": 25})
print(age1)
print(age2)
print(age3)
height = pd.Series({'Jerry': 170, "Natalie": 159, "John": 184, "Panda": 176})

data = pd.DataFrame({'age':age3, 'height':height, 'weight':(height - 4*age3)})
print(data)
print(data.iloc[:2, 2:4])
print()
print(data.loc[:'John', "age":"height"])
print()
print((data.weight > 40) & (data.age >22))
print(data[(data.weight > 70) | (data.age <= 20)])

print('\n')

A = pd.DataFrame(rng.randint(0, 10 ,(2,2)), columns = list("AB"), index = ['a', 'b'])
B = pd.DataFrame(rng.randint(0, 20 ,(3,3)), columns = list("ABC"), index = ['a', 'b', 'c'])
print(A); print(); print(B); print()

fill = A.stack().mean() #mean = average = 4.75
print(A+B)
print(A.add(B))
print(A.add(B, fill_value = fill))
print(A.add(B, fill_value = 0))

print('\n')

A = rng.randint(10, size = (3,4)) #array by rng.randint
print(A); print(); print(A - A[0]); print()
df = pd.DataFrame(A, columns = list('abcd'), index = list('ABC'))

print(df - df.iloc[0]); print(df - df.loc['A']) # same! loc[A] -> object, loc['A'] -> int

print()
print(df.iloc[0:2, 1:2])
print()
print(df.iloc[1,3])
print()
print(df['a'])
