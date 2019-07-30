import numpy as np


def snell(theta_inc, n1, n2):
    """
    Compute the refraction angle using Snell's law 
    
    see https://en.wikipedia.org
    
    Parameters
    __________
    theta_inc : float
        incident angle in radians
    n1, n2 : float
        the refractive index of medium of origin and destination medium
        
    Returns
    _________
    theta: float
        refraction angle
        
    Examples
    ______________
    a ray enters an air-water boundary at pi/4 radians (45 degress), comput exit angle. 
    
    >>> snell (snell(np.pi/4, 1.00, 1.33))
    """
    return "The answer to the snell equation"