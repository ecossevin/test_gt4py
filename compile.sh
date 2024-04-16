source ~/gt4py/.venv/bin/activate
#export PYTHONPATH=$PYTHONPATH:$HOME/dwarf-p-ice3/src
#export PYTHONPATH=$PYTHONPATH:$HOME/dwarf-p-ice3
#echo $PYTHONPATH

export PYTHONPATH=$PYTHONPATH:$HOME/ifs_physics_common

#gtpyc list-backends

echo "Set environment variables"
export BOOST_ROOT=/usr/include/boost
export CUDA_ROOT=/opt/softs/nvidia/hpc_sdk/Linux_x86_64/24.3/cuda
#export CUDA_ROOT=$HOME/cuda
export CUDA_PATH=/opt/softs/nvidia/hpc_sdk/Linux_x86_64/24.3/cuda
#export CUDA_PATH=$HOME/cuda
export CUDA_ARCH=sm_70
#export CUDA_ARCH=sm_70
#export CXX=$HOME/g++
#export CXX=$HOME/g++
#export CXX=/opt/softs/gcc/9.2.0/bin/g++
#export CXX=/usr/bin/g++
export CUDACXX=/opt/softs/nvidia/hpc_sdk/Linux_x86_64/24.3/cuda/nvcc
#export CUDACXX=$HOME/cuda/bin/nvcc

echo "Test compile stencils"
python3 ./example_erwan2.py
#python3 tests/stencils/test_compile_stencils.py
echo "Stencil compilation completed"
