import math
x = 100 ; print('sqrt(x)' , math.sqrt(x))

L = list(range(10)) ; print(L)

L2 = [str(c) for c in L]
print(L2)

x = 'I love you'
print(x)
type(x)
print(x[0:4])

#List Tuple    
List = ['Love', 520, "Jerry", 1234]
Tuple = (111, 'kwk1', 123)
print(List[0:2])
print(Tuple[0:3])

# +-*/sad
p = "Hello"
q = "123"
a = p+q
print(a)

p += q
print(p)
p += a
print(p)

x = 10 ; y = 20
if x == y:
    print('x = y')
elif x > y:
    print(x*y)
else:
    print('nothing')

while(input('>> ') != "bye"):
    print("so sad")

m = 270
print("I have {}, but I need {} more.".format(str(m), str(270*2-100))) 

print(list(range(10)))
print(list("abc"))

