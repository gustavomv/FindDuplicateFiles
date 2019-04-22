import os
import WriteOutput as wo

fileDict = {}
pathDict = {}

def GetFilePaths(searchDir):

	for dirpath, dirnames, filenames in os.walk(searchDir):
		
		for file in filenames:
			fullpath = os.path.normpath(os.path.join(dirpath, file))

			if file not in pathDict:
				pathDict[file] = [fullpath]
			else:
				pathDict[file].append(fullpath)
	
	for key in list(pathDict):
		if len(pathDict[key]) < 2:
			pathDict.pop(key,None)
	
	return pathDict


def GetFileExtension(searchDir):
	
	for dirpath, dirnames, filenames in os.walk(searchDir):
		
		for file in filenames:
			fileName, fileExt = os.path.splitext(file)
			
			if fileExt not in fileDict:
				fileDict[fileExt] = [file]
			else:
				fileDict[fileExt].append(file)
	
	return fileDict