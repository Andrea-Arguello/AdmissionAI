import numpy as np
from datasets import dataset_1
from desc_gradiente import *
from matplotlib import pyplot as plt

(X, y) = dataset_1
m, n = X.shape


theta_0 = np.random.rand(n, 1)
print(theta_0)

thetas, costs, gradient_norms = gradient_descent(X, y, theta_0, cost=linear_cost, cost_derivative=gradiente_linear_cost, alpha=0.0000000000000001)

print('THETA:', thetas)

print(theta_0)

plt.scatter(X[:, 1], y)

plt.plot(X[:, 1], np.matmul(X, thetas), color='red')

plt.show()