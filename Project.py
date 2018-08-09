from math import cos , sin , radians

print ("Welcome to point cloud rotator.")
print ("I can make a new text file with coordinates of rotated point cloud or generate file with rotation matrix for CloudCompare.")
print ("First of all type in Euler angles in degrees and scanner coordinates you are given.")

while True:
	alpha = radians (float (input ("Alpha: ")))
	beta = radians (float (input ("Beta: ")))
	gamma = radians (float (input ("Gamma: ")))

	deltaX = input ("x: ")
	deltaY = input ("y: ")
	deltaZ = input ("z: ")

	a11 = (cos(beta)*cos(gamma))
	a21 = (sin(alpha)*sin(beta)*cos(gamma) + cos(alpha)*sin(gamma))
	a31 = (-cos(alpha)*sin(beta)*cos(gamma) + sin(alpha)*sin(gamma))
	a12 = (-cos(beta)*sin(gamma))
	a22 = (-sin(alpha)*sin(beta)*sin(gamma) + cos(alpha)*cos(gamma))
	a32 = (cos(alpha)*sin(beta)*sin(gamma) + sin(alpha)*cos(gamma))
	a13 = (sin(beta))
	a23 = (-sin(alpha)*cos(beta))
	a33 = (cos(alpha)*cos(beta))

	a14 = deltaX
	a24 = deltaY
	a34 = deltaZ
	
	a41 = 0
	a42 = 0
	a43 = 0
	a44 = 1

	while True:
		print ("Do you want to generate rotation matrix (G) or rotate the cloud (R)?")
		choise = input ("Type in G or R: ")

		if choise == "G" or choise == "g":
			print ("Generating")
			break
		elif choise == "R" or choise == "r":
			print ("Rotating")
			break
		else:
			print ("Incorrect input")
			continue
