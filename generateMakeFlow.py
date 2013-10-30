outString = ""
for i in range(543):
    partNum = '%06d' % i
    outString += (("test1_density_grid.txt.part_%s ")%(partNum))
outString +=' : test1_density_grid.txt chunkFile.sh'
print(outString)
print("    ./sh chunkFile.sh test1_density_grid.txt 100000")


for i in range(543):
    partNum = '%06d' % i
    fileName = ("test1_density_grid.txt.part_%s" %(partNum))
    print(fileName+(".out: %s grav.py" %(fileName)))
    print(("grav.py test1_density_grid.txt.part_%s %s") % (partNum,"test1_grav_pos.txt"))
    print(("	./python grav.py %s %s") % (fileName,"test1_grav_pos.txt"))