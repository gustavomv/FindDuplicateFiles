import FilePath as fp
import CompareFiles as cp
import WriteOutput as wo

initPath = input("Enter the initial search path: ")
cands = fp.GetFilePaths(r"%s" %initPath)
dups = cp.CompFiles(cands)

wo.SetOutp('duplicate_candidates.txt', cands)
wo.SetOutp('duplicates.txt', dups)
print("Finished!!! :)")
