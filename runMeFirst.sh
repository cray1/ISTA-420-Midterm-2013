#!/bin/bash
export PATH=~/cctools/bin:${PATH}
export PYTHONPATH=${PYTHONPATH}:~/cctools/lib/python2.4/site-packages
python generateMakeFlow.py > mf.t
mv mf.t Makeflow
torque_submit_workers -a -N PamplemousseFullCalc 542 -c 0
makeflow -T wq -a -N PamplemousseFullCalc

