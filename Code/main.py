import FilePath as fp
import CompareFiles as cp
import WriteOutput as wo

initPath = input("Digite o caminho inicial de busca: ")
cands = fp.GetFilePaths(r"%s" %initPath)
dups = cp.CompFiles(cands)

wo.SetOutp('duplicate_candidates.txt', cands)
wo.SetOutp('duplicates.txt', dups)
print("Finished!!! :)")
