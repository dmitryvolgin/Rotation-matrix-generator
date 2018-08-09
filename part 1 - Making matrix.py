from math import cos , sin , radians
c = cos
s = sin
from decimal import *
# Translation
tx = 3316.32
ty = -78.2211
tz = 74.1439
# Rotation in degrees
alpha = -0.14435
beta = 1.63451
gamma = -0.395624
# Converting into radians
x = radians(alpha)
y = radians(beta)
z = radians(gamma)
# Rotation matrix (3x3)
a11 = str(c(y)*c(z))
a21 = str(s(x)*s(y)*c(z) + c(x)*s(z))
a31 = str(-c(x)*s(y)*c(z) + s(x)*s(z))
a12 = str(-c(y)*s(z))
a22 = str(-s(x)*s(y)*s(z) + c(x)*c(z))
a32 = str(c(x)*s(y)*s(z) + s(x)*c(z))
a13 = str(s(y))
a23 = str(-s(x)*c(y))
a33 = str(c(x)*c(y))
# Translation matrix
a14 = str(tx)
a24 = str(ty)
a34 = str(tz)
# Others
a41 = str(0)
a42 = str(0)
a43 = str(0)
a44 = str(1)
# Check the path!
file = open('C:\\Users\\dmitr\\Downloads\\Diplom\\Python test\\Making matrix\\006_matrix.txt','w')
# writing
matrix = a11+" "+a12+" "+a13+" "+a14+"\n"+a21+" "+a22+" "+a23+" "+a24+"\n"+a31+" "+a32+" "+a33+" "+a34+"\n"+a41+" "+a42+" "+a43+" "+a44
file.write(matrix)
file.close()
