from math import cos , sin , radians

print ("Welcome to point cloud rotator.")
print ("I can make a new text file with coordinates of rotated point cloud or generate file with rotation matrix for CloudCompare.")
print ("First of all type in Euler angles in degrees and scanner coordinates you are given.")


while True:
	cont = input ("Continue? (Y/N): ")
	if cont == "n" or cont == "N":
		break
	elif not cont == "y" and not cont == "Y":
		print ("Incorrect input!\nType in Y or N")
		continue

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

			matrix = str(a11)+" "+str(a12)+" "+str(a13)+" "+str(a14)+"\n"+str(a21)+" "+str(a22)+" "+str(a23)+" "+str(a24)+"\n"+str(a31)+" "+str(a32)+" "+str(a33)+" "+str(a34)+"\n"+str(a41)+" "+str(a42)+" "+str(a43)+" "+str(a44)
			print ("Enter the name for the matrix file.")
			matrix_name = input (": ")
			print ("Generating...")

			"""
			Записывает файл в директорию C:/Users/dmitr/(matrix)
			Исправить!
			"""

			with open (matrix_name, "w") as matrix_file:
				matrix_file.write (matrix)
				print ("Generation completed!")
			break

		elif choise == "R" or choise == "r":
			print ("Enter the path to txt file with your point cloud")
			initial_cloud = input (": ")
			print ("Rotating...")
			break
		else:
			print ("Incorrect input!")
			continue
