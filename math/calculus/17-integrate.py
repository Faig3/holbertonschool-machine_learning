#!/usr/bin/env python3
"""
Function that computes the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """
       Returns the integral of a polynomial
       """
    if (not isinstance(poly, list) or len(poly) == 0 or
            not all(isinstance(c, (int, float)) for c in poly) or
            not isinstance(C, (int, float))):
        return None
    else:
        poly.insert(0, C)
        if len(poly) > 2:
            for i in range(2,len(poly)):
                if poly[i] != 0:
                    poly[i] = poly[i] / i
                else:
                    continue
        return poly
