# -----------------------------------------------------------------------
# finds recorded flight data closest to the timeStamp indicated by frame
# for ortho-rectification in Headwall's SpectralView
# 
# 2/14/2020, Cal Poly Pomona
# email: fionchan@cpp.edu
# -----------------------------------------------------------------------
from pathlib import Path

folder = Path(input("Enter folder path: "))

start = "y"
while start == "y" or start == "Y":
	# find timeStamp from frameIndex.txt
	frame = input("Enter frame #: ")
	filepath = folder / ("frameIndex_" + str(frame) + ".txt")
	print(filepath)
	frameIndex = open(filepath, "rt")
	for i in [0,1]:
		line = frameIndex.readline()
	timeStamp = line.split('\t')[1]
	print("Indicated Timestamp: " + timeStamp)
	frameIndex.close()

	# read imu_gps.txt line by line
	# until find closest matching timeStamp (col6 == timeStamp)
	# col0 = roll; col1 = pitch; col2 = yaw; etc...
	# each col is delineated by '\t'
	imu_gps = open(folder / "imu_gps.txt", "rt")
	header = imu_gps.readline().split('\t',9)
	found = False;
	while found == False:
		row = imu_gps.readline().split('\t',9)
		nextRow = imu_gps.readline().split('\t',9)
		if nextRow:
			if nextRow[6] > timeStamp:
				found = True
				print("Found:")
				ts1 = int(row[6])
				nextRow = imu_gps.readline().split('\t',9)
				ts2 = int(nextRow[6])
				timeStamp = int(timeStamp)
				if abs(timeStamp - ts1) < abs(ts2 - timeStamp):
					for i in range(0,10):
						print(header[i] + ": " + row[i])
				else:
					for i in range(0,10): 
						print(header[i] + ": " + nextRow[i])
		else:
			break

	start = input("Search another frame? (y/n): ")

imu_gps.close()