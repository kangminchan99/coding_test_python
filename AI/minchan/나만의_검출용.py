import numpy as np
import sys
import os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

import pickle                       

def relu(x):
    return np.maximum(0, x)

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T 

    x = x - np.max(x) # 오버플로 대책
    return np.exp(x) / np.sum(np.exp(x))
    
def predict(param, x):
    W1, W2 = param['W1'], param['W2']
    b1, b2 = param['b1'], param['b2']
    
    a1 = np.dot(x, W1) + b1
    z1 = relu(a1)
    a2 = np.dot(z1, W2) + b2
    y = softmax(a2)
    
    return y

def accuracy(y, t):
    y = np.argmax(y, axis=1)
    if t.ndim != 1:
        t = np.argmax(t, axis=1)

    accuracy = np.sum(y == t) / float(y.shape[0])
    return accuracy

(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=False)
    
with open("my_params.pkl", "rb") as file:   # 추가 분 : 본인이 생성한 것 저장
    params = pickle.load(file)

y = predict(params, x_test)
accu = accuracy(y, t_test)

print("=== 예제 검출 결과 ===")
print("0번째 데이터 : ", y[0], t_test[0])
print("1000번째 데이터 : ", y[1000], t_test[1000])
print("5000번째 데이터 : ", y[5000], t_test[5000])
print()
print("=== 검출률 ===")
print("accuracy = ", accu)