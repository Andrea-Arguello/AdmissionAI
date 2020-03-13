import numpy as np
import copy

# def desc_gradiente(max_ite, alpha, theta_0, d_dj, x, y, tolerance):
#     theta = theta_0
#     i = 0
#     while tolerance and i < max_ite:
#         d_dj(theta, x, y)
#         theta -= alpha*theta
#         i += 1
#     return theta

# norm = lambda v: ((v**2).sum())**0.5
# does the same as np.linalg.norm()

# metros cuadrados de casas
# >>> x = np.random.randint(10,100,20).reshape(20,1)
# >>> X = np.hstack((np.ones(20).reshape(20,1), x))
# >>> y=(X[:, 1] * 10).reshape(20,1)
# >>> np.hstack((X, y))



'''
def gradient_descent(X, y, theta_0, cost, cost_derivative, alpha=0.01, threshold=0.001, max_iter=10000):
    theta, i = copy.deepcopy(theta_0), 0
    costs = []
    gradient_norms = []
    while np.linalg.norm(cost_derivative(X,y,theta)) > threshold and i < max_iter:
        theta -= alpha * cost_derivative(X,y,theta)
        i+=1
        costs.append(cost(X, y, theta))
        gradient_norms.append(cost_derivative(X, y, theta))
    return theta, costs, gradient_norms
'''
# X has shape (m, n), y has shape (m,1), theta has shape (n,1)
linear_cost = lambda X, y, theta_0: ((np.matmul(X, theta_0)-y)**2).sum() / (2*X.shape[0])

gradiente_linear_cost = lambda X, y, theta_0: np.matmul((np.matmul(X,theta_0)-y).T,X).T / X.shape[0]


def gradient_descent(X, y, theta_0, cost, cost_derivative, alpha=0.01, threshold=0.001, max_iter=10000, lambda_0=0):
    theta, i = copy.deepcopy(theta_0), 0
    costs = []
    gradient_norms = []
    while np.linalg.norm(cost_derivative(X,y,theta,lambda_0)) > threshold and i < max_iter:
        theta -= alpha * cost_derivative(X,y,theta,lambda_0)
        i+=1
        costs.append(cost(X, y, theta, lambda_0))
        gradient_norms.append(cost_derivative(X, y, theta, lambda_0))
    return theta, costs, gradient_norms



# We add the regularization part
linear_cost_reg = lambda X, y, theta_0, lambda_0: linear_cost(X, y, theta_0) + lambda_0*(theta_0**2).sum() / (2*X.shape[0]) 

gradiente_linear_cost_reg = lambda X, y, theta_0, lambda_0: gradiente_linear_cost(X, y, theta_0) + lambda_0*(theta_0).sum() / X.shape[0]
