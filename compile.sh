#source ~/gt4py/.venv/bin/activate
source ~/gt4py/.venv/bin/activate
#export PYTHONPATH=$PYTHONPATH:$HOME/dwarf-p-ice3/src
#export PYTHONPATH=$PYTHONPATH:$HOME/dwarf-p-ice3
#echo $PYTHONPATH

#export PYTHONPATH=$PYTHONPATH:$HOME/ifs_physics_common

#gtpyc list-backends

module purge
#module load gcc/9.2.0
#gcc/nvhpc24.3
module load gcc/nvhpc24.3
#module load nvhpc/24.3
#module load nvhpc-hpcx-cuda12/24.3

echo "Set environment variables"
echo $NVHPC_ROOT
export CPATH="/home/gmap/mrpm/cossevine/boost"
#export BOOST_ROOT=/usr/include/boost
export CUDA_ROOT=$NVHPC_ROOT/cuda
export CUDA_PATH=$CUDA_ROOT
export CUDA_ARCH=sm_70
export CUDACXX=$CXX
#export CUDACXX=$CUDA_ROOT/bin/nvcc

echo "Test compile stencils"
python3 example_erwan2.py
#python3 example_erwan2.py
#python3 tests/stencils/test_compile_stencils.py
echo "Stencil compilation completed"
