#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
My code goes here
"""
from __future__ import division
from __future__ import absolute_import

import sys
sys.path.append("lib")
import spectral

class SpecClust:
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
    def get_rows(self):
    	return self.s.get_rows()
    def get_cols(self):
    	return self.s.get_cols()
    def cluster(self):
    	self.s.cluster()
    def write_data(self,csv):
    	self.s.write_data(csv)
    def set_centers(self,x):
    	self.s.set_centers(x)
    	self.centers = x
    def set_gamma(self,x):
    	self.s.set_gamma(x)
    	self.gamma = x 
    def set_max_iters(self,x):
    	self.s.set_max_iters(x)
    	self.max_iters = x 
    def set_kernel(self,x):
    	self.s.set_kernel(x)
    	self.kernel = x
    def set_constant(self,x):
    	self.s.set_constant(x)
    	self.constant = x
    def set_order(self,x):
    	self.s.set_order(x)
    	self.order = x
    def get_assignment(self,x):
    	return self.s.get_assignment(x)
    def get_assignments(self):
    	f = []
    	for i in range(1, self.s.get_rows()+1):
    		f.append(self.s.get_assignment(i))
    	return f
