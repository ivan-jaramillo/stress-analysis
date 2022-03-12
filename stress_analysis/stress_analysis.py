"""Stress Analysis

Calculate stress at a point on a body.
"""

import tensorflow as tf
import numpy as np

def main():
    print("Stress Analysis at a Point")

    # Have the user input principal stressses for now.
    sigma_xx = int(input("sigma_xx = "))
    sigma_yy = int(input("sigma_yy = "))
    sigma_zz = int(input("sigma_zz = "))

    # Create a rank two tensor for stress.
    stress = np.array([(sigma_xx, 0, 0), (0, sigma_yy, 0), (0, 0, sigma_zz)])
    print(stress)


if __name__ == "__main__":
    main()
