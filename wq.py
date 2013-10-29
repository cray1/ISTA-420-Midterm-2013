#!/usr/bin/python
 
from work_queue import *
import sys

try:
    Q = WorkQueue(port = 9889)
    Q.specify_name("Pamplemousse")	
	
except:
    print "could not instantiate Work Queue master"
    sys.exit(1)

print "Listening on port %d." % Q.port

density = os.listdir('tempSplit')
print "in tempSplit"
print density
print density[1]
gravity = os.listdir('gravity')
print "in current dir"
print gravity[0]

print "Submitting 542 simulation tasks..."
for i in range(len(density)):
	print density[i]
	
	infile1 = "tempSplit"+density[i]
	print i
	infile2 = gravity[0]
	print infile2
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
        print "task (id# %d): %s (return result %s)" % (T.id, T.command, T.result)
        print T.output
q.specify_password_file(mypwfile)		
print "done."