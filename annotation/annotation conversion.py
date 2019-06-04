# check the xml file for fidget spinner and change it to cow
import os, re
file_all = []
for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".xml"):
            	old = os.path.join(root, file)
            	file_all.append(old)



for filename in file_all:
	cow = []
	xmax = []
	ymax = []
	xmin = []
	ymin = []
	
	out = filename.replace(".xml", ".txt")
	output = open(out, "w")
	
	my_file = open(filename, "r")
	
	for line in my_file:
		if "cow" in line:
			cow.append("cow")
		elif "<xmax>" in line:
			xmax.append(re.findall("\d+", line)[0])
		elif "<xmin>" in line:
			xmin.append(re.findall("\d+", line)[0])
		elif "<ymax>" in line:
			ymax.append(re.findall("\d+", line)[0])
		elif "<ymin>" in line:
			ymin.append(re.findall("\d+", line)[0])

	for i in range(len(cow)):
		xmaxi = int(xmax[i])
		xmini = int(xmin[i])
		ymaxi = int(ymax[i])
		ymini = int(ymin[i])
		width = (int(xmaxi)-int(xmini))/2560
		height = (int(ymaxi)-int(ymini))/1440	
		x_center = int(xmini)/2560+0.5*width
		y_center = int(ymini)/1440+0.5*height

		width, height, x_center, y_center = round(width,3), round(height,3), round(x_center,3), round(y_center,3)
		li = "0"+" "+ str(x_center)+" "+ str(y_center)+ " "+str(width)+ " "+str(height)+"\n"
		output.write(li)
	output.close()