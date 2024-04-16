from gt4py.cartesian import gtscript
import numpy as np
#from ifs_physics_common.framework.gtscript import stencil_collection
from ifs_physics_common.framework.config import GT4PyConfig
from ifs_physics_common.framework.stencil import stencil_collection, compile_stencil

#backend = "gt:cpu_ifirst"
backend = "cuda"
#backend = "gt:gpu"
#backend = "numpy"
#backend = "dace:gpu"

#@gtscript.stencil(backend=backend, rebuild=True)
@stencil_collection("example1")
def example_1(
    #from __externals__ import TSTEP #dict externals 
    foo: gtscript.Field[np.float64], 
    inn: gtscript.Field[np.float64], 
    bar: gtscript.Field[np.float64]):
        
    with computation(PARALLEL), interval(...):
        foo[0,  0,  0] = inn[1, 0, 0] - inn[0,  0,  0]

#    with computation(PARALLEL), interval(...):
#        bar[0,  0,  0] = foo[1, 0, 0] - foo[0,  0,  0]
   
##@gtscript.stencil(backend=backend, rebuild=True)
#@stencil_collection("example2")
#def example_2(
#    bar: gtscript.Field[np.float64],
#    foo: gtscript.Field[np.float64]
#):
#    
        

    
if __name__ == "__main__":
	config = GT4PyConfig(
		backend=backend, rebuild=True, validate_args=True, verbose=True)
	#
	
	_ = compile_stencil("example1", config)		
#	_ = compile_stencil("example2", config)		
	
#      externals={ "cste" : 1}

#	_ = compile_stencil("example1", config, externals=externals)		
#	_ = compile_stencil("example2", config, externals=externals)		
