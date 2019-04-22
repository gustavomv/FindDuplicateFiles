import FilePath as fp
import CompareFiles as cp
import WriteOutput as wo

cands = fp.GetFilePaths(r'D:\DESKTOP_FILES')
dups = cp.CompFiles(cands)

wo.SetOutp('duplicate_candidates.txt', cands)
wo.SetOutp('duplicates.txt', dups)