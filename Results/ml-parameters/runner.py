###############################################################################
# File  : runner.py
# Author: Tara Pandya
# Date  : Mon May  1 10:55:48 EDT 2017
###############################################################################
from __future__ import (division, absolute_import, print_function, )
#-----------------------------------------------------------------------------#
import numpy as np

import sys
import os
import re

from omnibus.scripts.omnibus_run import MultiRun
###############################################################################

class C5G7Run(MultiRun):
    inp     = 'c5g7_small.omn'
    fmt     = '{solver}-ss{size:03d}-vcyc{num_v:02d}-r{num_relax:02d}-rwt{relax_weight:1.1f}'.format
    basedir = 'results'

    def update(self, db, solver, size, num_v, num_relax, relax_weight):

        # Update eigen solver
        db['denovo']['solver']['solver'] = solver

        # Update upscatter solver subspace size
        updb = db['denovo']['solver']['upscatter']
        updb['subspace_size'] = size

        # Update multilevel number of v cycles
        pdb = updb['preconditioner']
        pdb['num_v_cycles'] = num_v

        # Update multilevel relax count
        pdb['relax_count'] = num_relax

        # Update multilevel relax weight
        pdb['relax_weight'] = relax_weight

        # Update parameters for power iteration
        s = "rqi"
        if solver == 'power_iteration':
            s = "pi"
            db['denovo']['solver']['tolerance'] = 1.0e-2
            db['denovo']['solver']['k_tolerance'] = 1.0e-5

        # Update name of run        
        name = '{}_{}_{}_{}_{}'.format(s,size,num_v,num_relax,relax_weight)
        db['run']['name'] = name


##---------------------------------------------------------------------------##

def main():
    # Add rqi back to the solver list
    inputs = {
        'solver' : ['power_iteration'],
        'size'   : [50, 100, 150],
        'num_v'  : [1, 2, 3],
        'num_relax' : [1, 2, 3],
        'relax_weight' : [0.8, 1.0, 1.2]
    }

    with C5G7Run() as run:
        run.product(inputs)

#-----------------------------------------------------------------------------#
if __name__ == '__main__':
    main()

###############################################################################
# end of runner.py
###############################################################################
