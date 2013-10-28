#!/usr/bin/python
 
from work_queue import *
import sys

try:
    Q = WorkQueue(port = 3464)
    Q.specify_name("Pamplemousse")
except:
    print "could not instantiate Work Queue master"
    sys.exit(1)

print "Listening on port %d." % Q.port

density = os.listdir('tempSplit')
print "in tempSplit"

print "Submitting 542 simulation tasks..."
for i in range(len(density)):
	print density
	
	infile1 = "test1_density_grid.txt.part_00000" + str(i)
	print "test1_density_grid.txt.part_00000" + str(i)
	infile2 = "test1_grav_pos.txt"
	print "I'm running yo"
	outfile = "test1_density_grid.txt.part_00000" + str(i) + ".out"
	print "test1_density_grid.txt.part_00000" + str(i) + ".out"
	command = "python grav.py %s %s > %s" % (infile1, infile2, outfile)
	
	T = Task(command)
	T.specify_file("grav.py", "grav.py", WORK_QUEUE_INPUT, cache = True)
	T.specify_file(infile1, infile1, WORK_QUEUE_INPUT, cache = False)
	T.specify_file(infile2, infile2, WORK_QUEUE_INPUT, cache = False)
	T.specify_file(outfile, outfile, WORK_QUEUE_OUTPUT, cache = False)
	
	taskid = Q.submit(T)
print "done."

print "Waiting for tasks to complete..."
while not Q.empty():
    T = Q.wait(5)
    if T:
        print "task (id# %d) complete: %s (return code %d)" % (T.id, T.command, T.return_status)

print "done."