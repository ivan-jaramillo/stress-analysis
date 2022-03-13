"""Stress Analysis

Calculate stress at a point on a body.
"""

import numpy as np

def main():
    print("Stress Analysis at a Point")

    # Have the user input principal stressses for now.
    sigma_xx = int(input("sigma_xx = "))
    sigma_yy = int(input("sigma_yy = "))
    sigma_zz = int(input("sigma_zz = "))
    # Default of diagonal stress
    sigma_xy = 0
    sigma_xz = 0
    sigma_yz = 0

    # Create a rank two tensor for stress.
    stress = np.mat([(sigma_xx, sigma_xy, sigma_xz),
                       (sigma_xy, sigma_yy, sigma_yz),
                       (sigma_xz, sigma_yz, sigma_zz)])
    print(stress)

# Traction
def tractionForce(sigma, n):
    # sigma is a stress matrix
    # n is a unit vector that is also a matrix 
    t = sigma*n # traction vector
    magt = (n.T*sigma*n).item()
    tn = magt*n
    tt = t-tn
    return t, tn, tt
    
# Consitutive relations
def strainFromStress(stress, E=200, nu=0.3, alpha=1, deltaT = 0):
    G = E/(2*(1+nu))
    e_xx = (stress[0,0] - nu*stress[1,1] - nu*stress[2,2])/E + alpha*deltaT
    e_yy = (stress[1,1] - nu*stress[0,0] - nu*stress[2,2])/E + alpha*deltaT
    e_zz = (stress[2,2] - nu*stress[1,1] - nu*stress[0,0])/E + alpha*deltaT
    e_xy = stress[0,1]/G
    e_xz = stress[0,2]/G
    e_yz = stress[1,2]/G
    strain = np.mat([(e_xx, e_xy, e_xz),
                       (e_xy, e_yy, e_yz),
                       (e_xz, e_yz, e_zz)])
    return strain

# Equilibrium Check - would need sympy to do derivs


if __name__ == "__main__":
    main()
