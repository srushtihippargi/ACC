def Student_Controller(t, x, param):
    import numpy as np
    vd = param["vd"]
    v0 = param["v0"]

    m = param["m"]
    Cag1 = param["Cag"]
    Cdg1 = param["Cdg"]
    v1 = x[1]
    d = x[0]

    lam = 26.0
    alpha = 0.3
    w = 7000000

    h = ((v1 - vd) ** 2) / 2
    B = d - (0.5 * ((v0 - v1) ** 2) / Cdg1) - 1.8 * v1
    
    # Define the matrix P as a 2x2 identity matrix
    P = np.array([[1, 0],
                  [0, w]])
    
    # Define the matrix A as a 5x2 matrix
    A = np.array([[(v1 - vd) / m, -1],
                  [((1.8/m) +((v1 - v0)/(Cdg1 * m))), 0],
                  [1 / m, 0],
                  [-1 / m, 0],
                  [0, -1]])

    # Define the vector b as a 5x1 vector
    b = np.array([-lam * h, (alpha * B) + (v0 - v1), Cag1, Cdg1, 0])

    # Define the vector q as a 2x1 zero vector
    q = np.zeros((2, 1))
    
    return A, b, P, q
