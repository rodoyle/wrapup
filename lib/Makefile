# Location of the Python header files
 
PYTHON_VERSION = 2.7
PYTHON_INCLUDE = /usr/include/python$(PYTHON_VERSION)
 
# Location of the Eigen and Boost Python include files and library
 
EIGEN_INC = /usr/include/eigen3
BOOST_INC = /usr/include
BOOST_LIB = /usr/lib

SOURCE = spectral
DEST = ../wrapup/spectral
 
$(DEST).so: $(DEST).o
	g++ --std=c++11 -shared -Wl,--export-dynamic $(DEST).o -L$(BOOST_LIB) -lboost_python -L/usr/python$(PYTHON_VERSION)/config -lpython$(PYTHON_VERSION) -o $(DEST).so
 
$(DEST).o: $(SOURCE).cpp
	g++ --std=c++11 -I$(PYTHON_INCLUDE) -I$(BOOST_INC) -I$(EIGEN_INC) -fPIC -c $(SOURCE).cpp -o $(DEST).o

clean:
	rm $(DEST).so $(DEST).o

