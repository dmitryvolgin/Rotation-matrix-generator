from math import cos , sin , radians
c = cos
s = sin
from decimal import *
# Translation
tx = 155.909
ty = -10.524
tz = -928.642
# Rotation in degrees
gamma = 1.98341
beta = 2.35209
alpha = -2.18419
# Converting into radians
a = radians(alpha)
b = radians(beta)
g = radians(gamma)
# Rotation matrix 1.1 (3x3)
a11 = cos(a)*cos(g)-sin(a)*cos(b)*sin(g)
a12 = -cos(a)*sin(g)-sin(a)*cos(b)*cos(g)
a13 = sin(a)*sin(b)
a21 = sin(a)*cos(g)+cos(a)*cos(b)*sin(g)
a22 = -sin(a)*sin(g)+cos(a)*cos(b)*cos(g)
a23 = -cos(a)*sin(b)
a31 = sin(b)*sin(g)
a32 = sin(b)*cos(g)
a33 = cos(b)

file = open ('C:\\Users\\dmitr\\Downloads\\Diplom\\Python test\\001.txt')
file_2 = open('C:\\Users\\dmitr\\Downloads\\Diplom\\Python test\\new_001.txt','w')
counter = 0
for line in file:
	coords = line.split(" ")
	x = float(coords[0])
	y = float(coords[1])
	z = float(coords[2])
	att = coords[3]
	# rotating
	x1 = x*a11 + y*a12 + z*a13
	y1 = x*a21 + y*a22 + z*a23
	z1 = x*a31 + y*a32 + z*a33
	# translating
	x2 = x1 + tx
	y2 = y1 + ty
	z2 = z1 + tz
	# writing
	new_line = str('{0:.5f}'.format(x2))+" "+str('{0:.5f}'.format(y2))+" "+str('{0:.5f}'.format(z2))+" "+att
	file_2.write(new_line)
	# Loading
	counter+=1
	if counter == 5000000:
		print("25%")
	if counter == 10000000:
		print("50%")
	if counter == 15000000:
		print("75%")
print("100%")
print(str(counter)+" points processed")
file.close()
file_2.close()
print("Finished")