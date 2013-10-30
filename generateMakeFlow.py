print("test1_density_grid.txt test1_grav_pos.txt chunkFile.sh joinFile.sh prism.py grav.py:")
print("test1_density_grid.txt chunkFile.sh")
print("    sh chunkFile.sh test1_density_grid.txt 100000")
for i in range(543):
    partNum = '%06d' % i
    print(("grav.py test1_density_grid.txt.part_%s %s") % (partNum,"test1_grav_pos.txt"))
    print(("	python grav.py test1_density_grid.txt.part_%s %s") % (partNum,"test1_grav_pos.txt"))