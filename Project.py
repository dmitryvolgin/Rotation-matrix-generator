from math import cos , sin , radians

# Welcome words
print ("Welcome to point cloud rotator.")
print ("I can make a new text file with coordinates of rotated point cloud or generate file with rotation matrix for CloudCompare.")
print ("First of all type in the path to your working directory.")
working_directory = input("Path: ")

# Main loop starts when the path to the working directory is determined
while True:
	cont = input (f"Continue with {working_directory}? (Y/N): ")
	
	# If user notices some mistake in the path or need to change the path he can break the Main loop and start the program again
	if cont == "n" or cont == "N":
		break
	
	# If everything is OK and we want to use the chosen directory: continue
	elif not cont == "y" and not cont == "Y":
		print ("Incorrect input!\nType in Y or N")
		continue
	
	# Here program needs your Euler angles and scanner coordinates
	print ("Type in Euler angles in degrees and scanner coordinates you are given.")
	alpha = radians (float (input ("Alpha: ")))
	beta = radians (float (input ("Beta: ")))
	gamma = radians (float (input ("Gamma: ")))

	deltaX = float (input ("x: "))
	deltaY = float (input ("y: "))
	deltaZ = float (input ("z: "))
 
	# Computing the rotation matrix for Euler angles chosen above
	a11 = (cos(beta)*cos(gamma))
	a21 = (sin(alpha)*sin(beta)*cos(gamma) + cos(alpha)*sin(gamma))
	a31 = (-cos(alpha)*sin(beta)*cos(gamma) + sin(alpha)*sin(gamma))
	a12 = (-cos(beta)*sin(gamma))
	a22 = (-sin(alpha)*sin(beta)*sin(gamma) + cos(alpha)*cos(gamma))
	a32 = (cos(alpha)*sin(beta)*sin(gamma) + sin(alpha)*cos(gamma))
	a13 = (sin(beta))
	a23 = (-sin(alpha)*cos(beta))
	a33 = (cos(alpha)*cos(beta))

	# Making matrix elements from scanner coordinates
	a14 = deltaX
	a24 = deltaY
	a34 = deltaZ
	
	# We do not need theese four elements but they have to be in complete matrix
	a41 = 0
	a42 = 0
	a43 = 0
	a44 = 1

	# A this moment rotation matrix is ready and we have to choose what to do next
	while True:
		print ("Do you want to generate rotation matrix (G) or rotate the cloud (R)?")
		choise = input ("Type in G or R: ")

		# We can choose Generation but in fact matrix is already generated. Here we just printing it to text file
		if choise == "G" or choise == "g":

			# Choosing the name for new text file with your matrix
			matrix = str(a11)+" "+str(a12)+" "+str(a13)+" "+str(a14)+"\n"+str(a21)+" "+str(a22)+" "+str(a23)+" "+str(a24)+"\n"+str(a31)+" "+str(a32)+" "+str(a33)+" "+str(a34)+"\n"+str(a41)+" "+str(a42)+" "+str(a43)+" "+str(a44)
			print ("Enter the name for the matrix file (without extension).")
			matrix_name = input (": ")
			print ("Generating...")

			# Writing into the text file and breaking this sub-loop, this returns us at the choice if we want to continue
			with open (working_directory + "\\" + matrix_name + ".txt", "w") as matrix_file:
				matrix_file.write (matrix)
				print ("Generation completed!")
			break

		# If we choosing Rotation, new text file with rotated point cloud will appear
		elif choise == "R" or choise == "r":

			# Enter the name of the file with your point cloud (IT MUST BE IN THE WORKING DIRECTORY!!!)
			print ("Enter your point cloud file name (with extension)")
			cloud_file_name = input (": ")
			print ("Preparing point cloud...")

			# Counting lines in initial file
			with open (working_directory + "\\" + cloud_file_name, "r") as initial_cloud:
				lines_total = sum (1 for line in initial_cloud)

			# Creating a new file and writing new coordinates of rotated point cloud in it 
			with open (working_directory + "\\" + cloud_file_name, "r") as initial_cloud:
				with open (working_directory + "\\" + cloud_file_name + "_ROTATED.txt", "w") as rotated_cloud:
					print ("Rotating...")
					lines_counter = 0
					print ("0%")
					for line in initial_cloud:
						coords = line.split(" ")
						
						# Skipping incorrect lines
						if not len(coords) == 4:
							continue
						
						# Reading coordinates from initial text file
						x = float(coords[0])
						y = float(coords[1])
						z = float(coords[2])
						attribute = coords[3]
						
						# Applying rotation
						x1 = x*a11 + y*a12 + z*a13
						y1 = x*a21 + y*a22 + z*a23
						z1 = x*a31 + y*a32 + z*a33
						
						# Applying translation
						x2 = x1 + deltaX
						y2 = y1 + deltaY
						z2 = z1 + deltaZ
						
						# Writing new coordinates to the new file
						new_line = str(format(x2,'.5f'))+" "+str(format (y2,'.5f'))+" "+str(format (z2,'.5f'))+" "+attribute
						rotated_cloud.write(new_line)
						
						# Loading module shows the progress every 2.000.000 iteration
						lines_counter += 1
						if lines_counter % 2000000 == 0:
							print (str(int(lines_counter/lines_total*100)) + "%")

			# Finishing and breaking this sub-loop, returning to the choice if we want to continue in the directory
			print ("100%")
			print("Finished")
			print(str(lines_counter)+" points processed")
			break
		
		else:
			print ("Incorrect input!")
			continue