# from sklearn.datasets import load_digits
# digits = load_digits()
# print(digits.data.shape)

# import matplotlib.pyplot as plt
# plt.matshow(digits.images[0])
# plt.show()
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

data = load_iris()
y = data.target
x = data.data
pca = PCA(n_components=2)
reduced_X = pca.fit_transform(x) 

red_x, red_y = [],[]
blue_x, blue_y = [],[]
green_x, green_y = [],[]

for i in range(len(reduced_X)):
    if y[i] == 0:
        red_x.append(reduced_X[i][0])
        red_y.append(reduced_X[i][1])
    elif y[i] == 1:
        blue_x.append(reduced_X[i][0])
        blue_y.append(reduced_X[i][1])
    else:
        green_x.append(reduced_X[i][0])
        green_y.append(reduced_X[i][1])

plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='x')
plt.scatter(green_x, green_y, c='g', marker='x')
plt.show()