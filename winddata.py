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
with open('sample_wind_data.txt') as winddatafile:
	for line in winddatafile:


		#Clear list dataline
		dataline = []

		#Check if first character is a %, if so, append header data to a list
		if line.startswith('%'):
			#Set required elements of each header row as vars
			year = line[13:17]
			month = line[18:20]
			day = line[21:23]
			hour = line[24:26]
			numlev = line[32:36]
			lat = line[55:62]
			lon = line[63:71]
		else:
			#Get information from subsection lines
			pressure = line[9:15]
			height = line[16:21]
			temp = line[22:27]
			wdir = line[40:45]
			wvel = line[47:52]


			#dataline is the full data for each line
			#TODO add all variables to printing
			dataline.append((year,month,day,hour,height,pressure,temp,wdir,wvel))

			fulldata.append(dataline)

#Open a file to output the data to
outputfile = open('output.txt','w')

#Print header row
outputfile.write('year,month,day,hour,height,pressure,temp,wdir,wvel\n')
for item in fulldata:
	outputfile.write('%s\n'%item)
