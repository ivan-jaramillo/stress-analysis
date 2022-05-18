import numpy as np

class stress(np.ndarray):
    # Inherits Numpy array class
    #
        def __new__(cls, a):
            # Create Array Object
            obj = np.asarray(a).view(cls)
            # Calculate a few things
            w,v = np.linalg.eig(obj)
            obj.principal_stress = w
            obj.principal_axes = v 
            return obj
        
        