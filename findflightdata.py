frame = input("Enter frame #: ")

filename = "frameIndex_" + frame + ".txt"
#print(filename)
frameIndex = open(filename, "r")
for i in [0,1]:
	line = frameIndex.readline()
#print(line)
timeStamp = line.split('\t')[1]
#print(timeStamp)
frameIndex.close()
line = ""

imu_gps = open("imu_gps.txt","r")
#read imu_gps line by line
#until find closest matching timeStamp (col7 == timeStamp)
#col1 = roll; col2 = pitch; col3 = yaw; etc...
#each col is delineated by '\t'

imu_gps.close()