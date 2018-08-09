print ("Welcome to point cloud rotator.")
print ("I can make a new text file with coordinates of rotated point cloud or generate file with rotation matrix for CloudCompare.")
print ("First of all type in Euler angles you are given.")

alpha = input ("Alpha: ")
beta = input ("Beta: ")
gamma = input ("Gamma: ")

while true:
	print ("Do you want to generate rotation matrix (G) or rotate the cloud (R)?")
	choise = input ("Type G or R: ")

	if choise == "G" or choise == "g":
		print ("Generating")
	elif choise == "R" or choise == "r":
		print ("Rotating")
	else:
		print ("Incorrect input")
