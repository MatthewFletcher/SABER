
#Pull information from file at link:
#README for data https://www1.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt


#Link to data page
# https://www1.ncdc.noaa.gov/pub/data/igra/data/data-por/
#File name: USM00072582-data.txt

#IMPORTANT: All section headers begin with a % instead of a #

#Import subsection reader
#import subsectionreader.py as ssr


#Create empty list for full data
fulldata = []

#Read file into python

filename  = 'USM00072582-data.txt'

with open(filename) as winddatafile:
	for line in winddatafile:


		#Clear list dataline
		dataline = []

		#Check if first character is a %, if so, append header data to a list
		if line.startswith('%'):
			#Set required elements of each header row as vars
			year = int(line[13:17])
			month = int(line[18:20])
			day = int(line[21:23])
			hour = int(line[24:26])
			numlev = int(line[32:36])
			lat = int(line[55:62])
			lon = int(line[63:71])
		else:
			#Get information from subsection lines
			pressure = int(line[9:15])
			if pressure == -9999:
				break
			height = int(line[16:21])
			if height == -9999:
				break
			temp = int(line[22:27])
			wdir = int(line[40:45])
			if wdir == -9999:
				break
			wvel = int(line[47:52])
			if wvel  == -9999:
				break

			#dataline is the full data for each line
			dataline.append((year,month,day,hour,height,pressure,temp,wdir,wvel))
			#Append current line of data as a list to the full data set
			fulldata.append(dataline)

#Open a file to output the data to
#outputfile = open('output.txt','w')

#Print header row
print('year,month,day,hour,height,pressure,temp,wdir,wvel')

#Print out data
for item in fulldata:
	if -9999 not in item:
	#print('%s\n'%item)
		for item2 in item:
			print('{0}'.format(item2))
