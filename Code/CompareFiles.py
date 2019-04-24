import itertools
import os
import hashlib

duplicates = {}

def CompFiles(FileDicData):

	for fileName in FileDicData:
		for path1, path2 in itertools.combinations(FileDicData[fileName], 2):
			file1Size = os.stat(path1).st_size
			file2Size = os.stat(path2).st_size

			if (file1Size == file2Size):
				file1Hash = hashfile(path1)
				file2Hash = hashfile(path2)
				#"KEY = HASH+FILENAME"
				if(file1Hash == file2Hash):
					if ((file1Hash+fileName) in duplicates):
						if (path1 not in duplicates[file1Hash+fileName]):
							duplicates[file1Hash+fileName].append(path1)
						if (path2 not in duplicates[file2Hash+fileName]):
							duplicates[file2Hash+fileName].append(path2)
					else:
						duplicates[file1Hash+fileName] = [path1]
						duplicates[file2Hash+fileName].append(path2)
					print("find duplicate! writing output...")
	print('\n')
	return duplicates

def hashfile(path, blocksize = 65536):
    
	afile = open(path, 'rb')
	hasher = hashlib.md5()
	buf = afile.read(blocksize)
    
	while len(buf) > 0:
		hasher.update(buf)
		buf = afile.read(blocksize)
	afile.close()
    
	return hasher.hexdigest()
