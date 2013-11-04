#generate the makeflow script for partitioning the density grid file. 
#File is assumed to be called test1_density_grid.txt
outString=""
for i in range(543): #number of files +1
    partNum = '%06d' % i
    outString += ("test1_density_grid.txt.part_%s " %(partNum))
print(outString+": test1_density_grid.txt chunkFile.sh")
print("	source chunkFile.sh test1_density_grid.txt 100000")

#generate the makeflow script for running each new partition through grav.py using test1_grav_pos.txt
for i in range(543): #number of files +1
    partNum = '%06d' % i
    fileName = ("test1_density_grid.txt.part_%s" %(partNum))
    outFile = fileName+".out"
    print(outFile+" : %s grav.py prism.py test1_grav_pos.txt" %(fileName))
    print(("    python grav.py %s test1_grav_pos.txt") % (fileName))

#generate the makeflow script for concatenating all the output files into one final file.
#final output file will be called test1_density_grid.txt.out
outString = "test1_density_grid.txt.out : " 
for i in range(543): #number of files +1
    partNum = '%06d' % i
    outString += ("test1_density_grid.txt.part_%s.out " %(partNum))
print(outString)
outString="cat"
for i in range(543): #number of files +1
    partNum = '%06d' % i
    outString += (" test1_density_grid.txt.part_%s.out" %(partNum))
print("    "+outString + " > test1_density_grid.txt.out") 
