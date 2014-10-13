#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import

import sys
sys.path.append("lib")
import spectral

# Python spectral clustering class
class SpecClust:

	## Constructor using CSV file containing raw data
    def __init__(self,csv):
        self.s = spectral.Spectral()
        self.s.read_data(csv)
        self.centers = 2
        self.kernel_type = 1
        self.normalise = 1
        self.max_iters = 1000
        self.gamma = 0.001
        self.constant = 1.0
        self.order = 2.0
    ## Check number of rows/observations that have been read    
    def get_rows(self):
    	return self.s.get_rows()
    ## Check number of columns/features that have been read  
    def get_cols(self):
    	return self.s.get_cols()
    ## Perform spectral clustering	
    def cluster(self):
    	self.s.cluster()
    ## Write data to csv file	
    def write_data(self,csv):
    	self.s.write_data(csv)
    ## Set number of centroids to cluster into	
    def set_centers(self,x):
    	self.s.set_centers(x)
    	self.centers = x
    ## Set RBF kernel gamma parameter	
    def set_gamma(self,x):
    	self.s.set_gamma(x)
    	self.gamma = x 
    ## Set max. iterations for k-means	
    def set_max_iters(self,x):
    	self.s.set_max_iters(x)
    	self.max_iters = x 
    ## Set kernel type - default (1) is RBF. 2 = polynomial	
    def set_kernel(self,x):
    	self.s.set_kernel(x)
    	self.kernel = x
    ## Set constant in polynomial kernel	
    def set_constant(self,x):
    	self.s.set_constant(x)
    	self.constant = x
    ## Set order in polynomial kernel		
    def set_order(self,x):
    	self.s.set_order(x)
    	self.order = x
    ## Get cluster assignment for row x	
    def get_assignment(self,x):
    	return self.s.get_assignment(x)
    ## Get all cluster assignments	
    def get_assignments(self):
    	f = []
    	for i in range(1, self.s.get_rows()+1):
    		f.append(self.s.get_assignment(i))
    	return f

