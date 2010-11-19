import sys
import zipfile
import os.path

default_report = "/home/ieeestudent/Downloads/MAME/torrent/romsReport.txt"
default_base = "/home/ieeestudent/Downloads/MAME/fix/"
default_dir = "/home/ieeestudent/Downloads/MAME/fix"

def parse_report(report_filename, patch_filename, output_dir):
	file_to_find = os.path.basename(patch_filename)
	print "About to process " + file_to_find
	with open(report_filename, 'r') as report:
		lines = report.readlines()
		for (index, line) in enumerate(lines):
			if (line.find(file_to_find) != -1):
				i = index
				while (i > 0):
					tokens = lines[i].split()
					if( (len(tokens) >= 3) and (tokens[0] == "In") and (tokens[1] == "game") ):
						# tokens[2] is the name of the rom.
						print "about to create " + tokens[2][:-1]
						zipfilename = os.path.join(output_dir, tokens[2][:-1] + ".zip")
						myzip = zipfile.ZipFile(zipfilename, 'a')
    						myzip.write(patch_filename, os.path.basename(patch_filename))
    						myzip.close()
    						i = 0
    					else:
    						i = i - 1		
			

argc = len(sys.argv)

if(argc == 2):
	to_process = os.path.join(default_base, sys.argv[1])
	parse_report(default_report, to_process, default_dir)
	print "Done!"
	
if(argc == 3):
	if(sys.argv[1] == "-d"):
		print "Looking in directory: " + sys.argv[2]
		for root, dirs, files in os.walk(sys.argv[2]):
			for name in files:
				parse_report(default_report, os.path.join(root, name), default_dir)
	 
elif(argc == 4):
	parse_report(sys.argv[1], sys.argv[2], sys.argv[3])
	
else:
	print "Usage:\npython patch.py <file in /fix to replace with>\n\t\t--OR--\npython patch.py <path to rom report> <full path to file> <path to output zips>"
    							
						
