// Spectral clustering, by Tim Nugent 2014

#ifndef SPECTRAL_H
#define SPECTRAL_H

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <Eigen/Dense>
#include <Eigen/Eigenvalues>
#include <boost/python.hpp>

using namespace Eigen;
using namespace std;
using namespace boost::python;

class Spectral{

public:
	Spectral() : centers(2), kernel_type(1), normalise(1), max_iters(1000), gamma(0.001), constant(1.0), order(2.0) {}
	explicit Spectral(MatrixXd& d) : centers(2), kernel_type(1), normalise(1), max_iters(1000), gamma(0.001), constant(1.0), order(2.0) {X = d;}
	int read_data(const char* data);
	int write_data(const char* data);
	int get_rows(){return X.rows();}
	int get_cols(){return X.cols();}
	void set_centers(const unsigned int i){centers = i;cout << "cpp: centers = " << centers << endl;};
	void set_kernel(const unsigned int i){kernel_type = i;};	
	void set_normalise(const unsigned int i){normalise = i;};
	void set_gamma(const double i){gamma = i;cout << "cpp: gamma = " << gamma << endl;};
	void set_constant(const double i){constant = i;};
	void set_order(const double i){order = i;};
	void set_max_iters(const unsigned int i){max_iters = i;};
	void cluster();
	const int get_assignment(unsigned int i) const {if(i <= X.rows()){return assignments[i-1];}else{return -1;};};
	const vector<int> &get_assignments() const {return assignments;};
private:
	void generate_kernel_matrix();
	double kernel(const VectorXd& a, const VectorXd& b);
	void eigendecomposition();
	void kmeans();
	MatrixXd X, K, eigenvectors;
	VectorXd eigenvalues, cumulative;
	unsigned int centers, kernel_type, normalise, max_iters;
	double gamma, constant, order;
	vector<int> assignments;
};

BOOST_PYTHON_MODULE(spectral){

	class_<Spectral>("Spectral")
	    .def("read_data", &Spectral::read_data)
	    .def("write_data", &Spectral::write_data)
	    .def("set_gamma", &Spectral::set_gamma)
	    .def("set_centers", &Spectral::set_centers)
	    .def("cluster", &Spectral::cluster)
	    .def("set_order", &Spectral::set_order)
	    .def("set_constant", &Spectral::set_constant)
	    .def("set_max_iters", &Spectral::set_max_iters)
	    .def("set_kernel", &Spectral::set_kernel)
	    .def("set_normalise", &Spectral::set_normalise)	    
	    .def("get_rows", &Spectral::get_rows)
	    .def("get_cols", &Spectral::get_cols)
	    .def("get_assignment", &Spectral::get_assignment)		  
	;
}

#endif
