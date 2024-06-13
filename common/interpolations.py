from py_matrix import Matrix


def lagrange_interpoplation(points, x):
    result = 0
    for i, pointi in enumerate(points):
        term = 1
        for j, pointj in enumerate(points):
            if i != j:
                term *= (x - pointj[0]) / (pointi[0] - pointj[0])
        result += term * pointi[1]
    return result

def cubic_spline_matrix(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    n = len(x) - 1
    h = [x[i+1] - x[i] for i in range(n)]
    
    A = Matrix(n+1,n+1,0)
    b = Matrix(n+1,1,0)
    A[(0,0)] = 1
    A[(n,n)] = 1
    
    for i in range(1, n):
        A[(i,i-1)] = h[i-1]
        A[(i,i)] = 2 * (h[i-1] + h[i])
        A[(i,i+1)] = h[i]
        b[(i,0)] = 3 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])
    
    return A, b, h

def spline_interpolation(points, x):
    A, b, h = cubic_spline_matrix(points);
    coeffs = A | b

    coeffs = [elem[0] for elem in coeffs.to_list()]
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]

    a = [ys[i] for i in range(len(points) - 1)]
    b = [(ys[i + 1] - ys[i]) / h[i] - h[i] * (2 * coeffs[i] + coeffs[i + 1]) / 3 for i in range(len(points) - 1)]
    d = [(coeffs[i + 1] - coeffs[i]) / (3 * h[i]) for i in range(len(points) - 1)]

    for i in range(len(points) - 1):
        if xs[i] <= x <= xs[i + 1]:
            dx = x - xs[i]
            return a[i] + b[i] * dx + coeffs[i] * dx ** 2 + d[i] * dx ** 3
    raise ValueError("x is outside the range of the given nodes.")