import os

def WriteText(OutputName, filePaths, nextPath):

	fout = open(OutputName, 'a')

	if nextPath == True:
		fout.write(filePaths)
		fout.write('; ')
	else:
		fout.write(filePaths)
		fout.write('\n\n')

def SetOutp(OutputName, Dict):
	for key in list(Dict):
		j = len(Dict[key])
		for i in range(len(Dict[key])):
			fullPath = os.path.normpath(os.path.join(Dict[key][i]))
				
			if j > 1:
				nextPath = True
			else:
				nextPath = False
			WriteText(OutputName, fullPath, nextPath)
			j -= 1
