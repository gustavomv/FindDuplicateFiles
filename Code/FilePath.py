import os
import WriteOutput as wo

candidates = {}

def GetFilePaths(searchDir):
	for dirpath, dirnames, filenames in os.walk(searchDir):	
		for file in filenames:
			fullpath = os.path.normpath(os.path.join(dirpath, file))
			print("file found here! fullpath: "+fullpath+'\n')
			if file not in candidates:
				candidates[file] = [fullpath]
			else:
				candidates[file].append(fullpath)
	print('\n')
	for key in list(candidates):
		if len(candidates[key]) < 2:
			candidates.pop(key,None)
		else:
			print("candidate file: "+key+'\n')
	print('\n')
	return candidates

def ErrorCall():
	print("Invalid Path! :(")
	exit()
	return 0
