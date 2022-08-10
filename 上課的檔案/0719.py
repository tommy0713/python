import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures


x_train = np.linspace(-5, 5, 10)
y_train = x_train + np.random.randn(10)

x_test = np.linspace(-5, 5, 100)
y_test = x_test + np.random.randn(100)

x_train = x_train.reshape(-1,1)
x_test = x_test.reshape(-1,1)

model = LinearRegression()


plt.figure(figsize=(20,10))
plt.scatter(x_train, y_train, s=50)        
for d in range(2, 11, 1):
    poly = PolynomialFeatures(degree=d, include_bias=False)
    x2 = poly.fit_transform(x_train)

    model.fit(x2,y_train)
    y_pred = model.predict(x2)

   
    print(f'R2_score of training set with {d}-degree = {r2_score(y_train, y_pred)}')

    x2_test = poly.fit_transform(x_test)
    y_test_pred = model.predict(x2_test)
    plt.plot(x_test, y_test_pred, lw=2, label = f'{d}-degree')
    print(f'R2_score of testing set with {d}-degree = {r2_score(y_test, y_test_pred)}')

plt.legend()
plt.show()