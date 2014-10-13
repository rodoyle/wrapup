# Python wrapper for spectral clustering C++ implementation

This code demonstrates how to implement a simple Python wrapper for a C++ class using Boost Python. The C++ code is an implementation of spectral clustering; this is a method which clusters data using the eigenvectors (spectrum) of the kernel matrix of the data. There are four main steps in the C++ code:

1. Computing the kernel matrix from the data. Polynomial and radial basis kernel functions are provided
2. Perform eigendecomposition on the matrix
3. Cluster k eignevectors/eigenvalues using standard k-means
4. Pass cluster assignements back to original data

Spectral clustering is useful for dimensionality reduction and is applicable to a wide range of problems in bioinformatics, e.g.

http://www.sciencedirect.com/science/article/pii/S0377042706002366
http://www.biomedcentral.com/1471-2105/11/403
http://nar.oxfordjournals.org/content/34/5/1571.short
http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0046468

## Compiling

Code has been tested under Ubuntu 14.04 and requires the following packages to be installed:

build-essential # gcc/g++ tools
libeigen3-dev # Linear algebra library for spectral clustering
libboost-python1.54.0 # Boost Python wrapper
libboost-python1.54-dev # Boost Python wrapper
r-base #  Optional, to visualise test output

sudo apt-get install build-essential libeigen3-dev libboost-python1.54.0 libboost-python1.54-dev r-base

To build the code, cd into the lib directory and type make. This will build the spectral.so shared object which can be imported by Python.

## Testing

Backup one directory and type 'py.test -s tests/test_things.py'. Output should be as follows. Any lines starting with cpp are called using C++ code.

====================================================================================== test session starts =======================================================================================
platform linux2 -- Python 2.7.6 -- py-1.4.25 -- pytest-2.6.3
collected 3 items 

tests/test_things.py 
Testing read_csv() function...

cpp: reading data/spirals.csv
cpp: reading finished
.
Testing cluster() function...

cpp: reading data/spirals.csv
cpp: reading finished
cpp: centers = 2
cpp: gamma = 172.05
cpp: generating kernel matrix...
cpp: eigendecomposition...
cpp: kmeans...
cpp: Iterations 1 : Error 0.4152 : Error delta 0.4152 : Centroid movement 0.0265
cpp: Iterations 2 : Error 0.2130 : Error delta 0.2022 : Centroid movement 0.0000
cpp: Iterations 3 : Error 0.2130 : Error delta 0.0000 : Centroid movement 0.0000
cpp: all done.
.
Testing write_csv() function...

cpp: reading data/spirals.csv
cpp: reading finished
cpp: centers = 2
cpp: gamma = 172.05
cpp: generating kernel matrix...
cpp: eigendecomposition...
cpp: kmeans...
cpp: Iterations 1 : Error 1.3037 : Error delta 1.3037 : Centroid movement 0.0503
cpp: Iterations 2 : Error 0.3881 : Error delta 0.9156 : Centroid movement 0.0302
cpp: Iterations 3 : Error 0.2134 : Error delta 0.1748 : Centroid movement 0.0014
cpp: Iterations 4 : Error 0.2130 : Error delta 0.0004 : Centroid movement 0.0000
cpp: Iterations 5 : Error 0.2130 : Error delta 0.0000 : Centroid movement 0.0000
cpp: all done.
cpp: writing data/clustered.csv
cpp: writing finished
.

=================================================================================== 3 passed in 41.47 seconds ====================================================================================

Three tests are run which check the main functionality:

1. Instantiation of a Python SpecClust object using the 'data/spirals.csv' file containing raw data. Test ensures a 300x2 matrix is read in correctly
2. Cluster function completes successfully and reasonable class assignments are made for all observations
3. Data is written to 'data/clustered.csv' including class assignments - needs write access to data directory

If R is installed, you can also run 'scripts/plot.R'. This will generate 'data/clustered.png' which shows the cluster assignments for the spirals data set.

## Notes

- The wrapper is implemented using Boost Python. I'm a fan of the Boost libraries and they are well maintained and documented, as well as explicitly supporting C++. 
- The Boost code exposes the main public functions in the 'spectral.h' file. 
- Importing and calling from Python is straightforward - I've made a very simple Python class in my_code.py to provide the interface.
- To-do: some checking that parameters passed in are numeric/reasonable values.
- To-do: data integrity on raw data.
- To-do: interface to pass a Python numpy matrix to the C++ library.

## Bugs

timnugent@gmail.com

