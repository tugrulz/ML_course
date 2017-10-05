# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
    print(x.shape[0])
    print(degree)
    degree=degree+1
    ext = np.zeros((x.shape[0], degree))
    for i in range (0,ext.shape[0]):
        for j in range (0,ext.shape[1]):
            ext[i][j] = x[i]**j
    return ext