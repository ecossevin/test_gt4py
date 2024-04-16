from gt4py.cartesian import gtscript
import numpy as np

backend = "gt:cpu_ifirst"
#backend = "numpy"
#backend = "dace:gpu"

@gtscript.stencil(backend=backend, rebuild=True)
def example_1(
    foo: gtscript.Field[np.float64], 
    inn: gtscript.Field[np.float64], 
    bar: gtscript.Field[np.float64]):
        
    with computation(PARALLEL), interval(...):
        foo[0,  0,  0] = inn[1, 0, 0] - inn[0,  0,  0]
    
@gtscript.stencil(backend=backend, rebuild=True)
def example_2(
    bar: gtscript.Field[np.float64],
    foo: gtscript.Field[np.float64]
):
    
    with computation(PARALLEL), interval(...):
        bar[0,  0,  0] = foo[1, 0, 0] - foo[0,  0,  0]
        

    
if __name__ == "__main__":
    
    from gt4py.storage import ones, zeros
        
    inn = ones((12, 12, 1), dtype=np.float64, backend=backend)
    inn[...] = np.random.rand(12, 12, 1)
    
    foo = ones((12, 12, 1), dtype=np.float64, backend=backend)
    foo[...] = np.random.rand(12, 12, 1)
    
    bar = ones((12, 12, 1), dtype=np.float64, backend=backend)
    bar[...] = np.random.rand(12, 12, 1)
    
    example_1(foo, inn, bar)
    example_2(bar, foo)
    
    
    
