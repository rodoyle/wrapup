#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import

from wrapup import spectral

class SpecClust:
    'Python spectral clustering class'

    def __init__(self,csv):
        'Constructor using CSV file containing raw data'
        self.s = spectral.Spectral()
        self.s.read_data(csv)
        self.centers = 2
        self.kernel_type = 1
        self.normalise = 1
        self.max_iters = 1000
        self.gamma = 0.001
        self.constant = 1.0
        self.order = 2.0
    def get_rows(self):
        'Check number of rows/observations that have been read'
    	return self.s.get_rows()
    def get_cols(self):
        'Check number of columns/features that have been read'
    	return self.s.get_cols()
    def cluster(self):
        'Perform spectral clustering'
    	self.s.cluster()
    def write_data(self,csv):
        'Write data to csv file'
    	self.s.write_data(csv)
    def set_centers(self,x):
        'Set number of centroids to cluster into'
    	self.s.set_centers(x)
    	self.centers = x
    def set_gamma(self,x):
        'Set RBF kernel gamma parameter'
    	self.s.set_gamma(x)
    	self.gamma = x 
    def set_max_iters(self,x):
        'Set max. iterations for k-means'
    	self.s.set_max_iters(x)
    	self.max_iters = x 
    def set_kernel(self,x):
        'Set kernel type - default (1) is RBF. 2 = polynomial'
    	self.s.set_kernel(x)
    	self.kernel = x
    def set_constant(self,x):
        'Set constant in polynomial kernel'
    	self.s.set_constant(x)
    	self.constant = x
    def set_order(self,x):
        'Set order in polynomial kernel'
    	self.s.set_order(x)
    	self.order = x
    def get_assignment(self,x):
        'Get cluster assignment for row x'
    	return self.s.get_assignment(x)
    def get_assignments(self):
        'Get all cluster assignments'
    	f = []
    	for i in range(1, self.s.get_rows()+1):
    		f.append(self.s.get_assignment(i))
    	return f

