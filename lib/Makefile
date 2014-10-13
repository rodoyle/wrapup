# Location of the Python header files
 
PYTHON_VERSION = 2.7
PYTHON_INCLUDE = /usr/include/python$(PYTHON_VERSION)
 
# Location of the Eigen and Boost Python include files and library
 
EIGEN_INC = /usr/include/eigen3
BOOST_INC = /usr/include
BOOST_LIB = /usr/lib

TARGET = spectral
 
$(TARGET).so: $(TARGET).o
	g++ --std=c++11 -shared -Wl,--export-dynamic $(TARGET).o -L$(BOOST_LIB) -lboost_python -L/usr/python$(PYTHON_VERSION)/config -lpython$(PYTHON_VERSION) -o $(TARGET).so
 
$(TARGET).o: $(TARGET).cpp
	g++ --std=c++11 -I$(PYTHON_INCLUDE) -I$(BOOST_INC) -I$(EIGEN_INC) -fPIC -c $(TARGET).cpp -o $(TARGET).o

clean:
	rm $(TARGET).so $(TARGET).o

