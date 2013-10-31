outString = ""
for i in range(543): #number of files +1
    partNum = '%06d' % i
    outString += ("test1_density_grid.txt.part_%s " %(partNum))
print(outString+": chunkFile.sh test1_density_grid.txt")
print("     (chunkFile.sh test1_density_grid.txt 100000)")
for i in range(543): #number of files +1
    partNum = '%06d' % i
    fileName = ("test1_density_grid.txt.part_%s" %(partNum))
    outFile = fileName+".out"
    print(outFile+": grav.py %s processWorker.sh" %(fileName))
    print(("    (processWorker.sh %s)") % (fileName))

#outString = "test1_density_grid.txt.out: " 
#for i in range(543): #number of files +1
#    partNum = '%06d' % i
#    outString += ("outFiles/test1_density_grid.txt.part_%s.out " %(partNum))
#print(outString)
#outString="cat"
#for i in range(543): #number of files +1
#    partNum = '%06d' % i
#    outString += (" outFiles/test1_density_grid.txt.part_%s.out" %(partNum))
#print("    "+outString + " > test1_density_grid.txt.out")

    
    