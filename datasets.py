import numpy as np

TRAINING_ELEMENTS = 200
x = np.linspace(
    -30,
    30,
    TRAINING_ELEMENTS
)

X = np.vstack(
    (
        np.ones(TRAINING_ELEMENTS),
        x,
        x**2,
        x**3,
        x**4
    )
).T

y = 5 + 2 * x ** 3 + np.random.randint(-15, 15, TRAINING_ELEMENTS)

dataset_1 = (X, y.reshape(TRAINING_ELEMENTS, 1))