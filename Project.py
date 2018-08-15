from math import cos , sin , radians

print ("Welcome to point cloud rotator.")
print ("I can make a new text file with coordinates of rotated point cloud or generate file with rotation matrix for CloudCompare.")
print ("First of all type in the path to your working directory.")
working_directory = input("Path: ")

while True:
	cont = input (f"Continue with {working_directory}? (Y/N): ")
	if cont == "n" or cont == "N":
		break
	elif not cont == "y" and not cont == "Y":
		print ("Incorrect input!\nType in Y or N")
		continue
	print ("Type in Euler angles in degrees and scanner coordinates you are given.")
	alpha = radians (float (input ("Alpha: ")))
	beta = radians (float (input ("Beta: ")))
	gamma = radians (float (input ("Gamma: ")))

	deltaX = float (input ("x: "))
	deltaY = float (input ("y: "))
	deltaZ = float (input ("z: "))

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
			print ("Enter the name for the matrix file (without extension).")
			matrix_name = input (": ")
			print ("Generating...")

			with open (working_directory + "\\" + matrix_name + ".txt", "w") as matrix_file:
				matrix_file.write (matrix)
				print ("Generation completed!")
			break

		elif choise == "R" or choise == "r":
			print ("Enter your point cloud file name (with extension)")
			cloud_file_name = input (": ")
			print ("Preparing point cloud...")

			with open (working_directory + "\\" + cloud_file_name, "r") as initial_cloud:
				lines_total = sum (1 for line in initial_cloud)

			with open (working_directory + "\\" + cloud_file_name, "r") as initial_cloud:
				with open (working_directory + "\\" + cloud_file_name + "_ROTATED.txt", "w") as rotated_cloud:
					print ("Rotating...")
					lines_counter = 0
					print ("0%")
					for line in initial_cloud:
						coords = line.split(" ")
						
						if not len(coords) == 4:
							continue
						
						x = float(coords[0])
						y = float(coords[1])
						z = float(coords[2])
						attribute = coords[3]
						# rotating
						x1 = x*a11 + y*a12 + z*a13
						y1 = x*a21 + y*a22 + z*a23
						z1 = x*a31 + y*a32 + z*a33
						# translating
						x2 = x1 + deltaX
						y2 = y1 + deltaY
						z2 = z1 + deltaZ
						# writing
						new_line = str(format(x2,'.5f'))+" "+str(format (y2,'.5f'))+" "+str(format (z2,'.5f'))+" "+attribute
						rotated_cloud.write(new_line)
						# Loading
						lines_counter += 1
						loading = lines_counter/lines_total
						if loading == 0.2:
							print ("20%")
						if loading == 0.4:
							print ("40%")
						if loading == 0.6:
							print ("60%")
						if loading == 0.8:
							print ("80%")

			print ("100%")
			print("Finished")
			print(str(lines_counter)+" points processed")
			break
		
		else:
			print ("Incorrect input!")
			continue