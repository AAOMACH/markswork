from cmath import sqrt

a = int(input("x2: "))
b = int(input("x: "))
c= int(input("z: "))


d = b*b

e = d - 4*a*c
f = sqrt(e)
g = b-f
k = 2*a
h = g/k
print("The first root is %s"% str(h))

i = b+f
j = i/k

print("The second root is %s" % str(j))
