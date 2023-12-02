from random import randint
from sklearn.linear_model import LinearRegression

TRAIN_SET_LIMIT = 1000

TRAIN_SET_COUNT = 100

TRAIN_INPUT = list()
TRAIN_OUTPUT = list()

for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    # print(a, b, c)
    op = a + 2 * b + 3 * c
    # print(op)
    TRAIN_INPUT.append([a, b, c])
    # print(TRAIN_INPUT)
    TRAIN_OUTPUT.append(op)
    # print(TRAIN_OUTPUT)

predictor = LinearRegression(n_jobs=1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

X_TEST = [[10, 20, 30]]

outcome = predictor.predict(X=X_TEST)

coefficients = predictor.coef_
print(coefficients)

print('Outcome: {}\nCoefficients: {}'.format(outcome, coefficients))
