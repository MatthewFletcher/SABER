#Function to read subsections of headers


#This function will be called in a for loop
#going through each line


#for line in datafile:
	pressure = line[9:14]
	height = line[16:20]
	temp = line[22:26]
	wdir = line[40:44]
	wvel = line[47:51]
