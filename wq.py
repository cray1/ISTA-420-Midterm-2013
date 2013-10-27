#!/usr/bin/env python

from work_queue import *
import sys

try:
    Q = WorkQueue(port = 0)
except:
    print "could not instantiate Work Queue master"
    sys.exit(1)

print "Listening on port %d." % Q.port

print "Submitting 542 simulation tasks..."
for i in range(0, 542):
    infile = "input.txt"
    outfile = "file.%0.2x" % i
    command = "python simulation.py %d < %s > %s" % (i, infile, outfile)

    T = Task(command)

    T.specify_file("simulation.py", "simulation.py", WORK_QUEUE_INPUT, cache = True)
    T.specify_file(infile, infile, WORK_QUEUE_INPUT, cache = False)
    T.specify_file(outfile, outfile, WORK_QUEUE_OUTPUT, cache = False)

    taskid = Q.submit(T)
print "done."

print "Waiting for tasks to complete..."
while not Q.empty():
    T = Q.wait(5)
    if T:
        print "task (id# %d) complete: %s (return code %d)" % (T.id, T.command, T.return_status)

print "done."