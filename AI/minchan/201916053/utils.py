import sys, os
sys.path.append("C:/Users/CE406/Documents/201916053_강민찬/DeepLearningProject")
import numpy as np
from collections import OrderedDict

def sigmoid(x):
    return 1 / (1+np.exp(-x))


def softmax(x):
    if x.ndim == 1:
        x = x.T
        x = x -np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T
    
    x = x - np.max(x)
    return np.exp(x) / np.sum(np.exp(x))


def sigmoid_grad(x):
    return (1.0 - sigmoid(x) * sigmoid(x))
    


def cross_entropy_error(y,t):
    if y.dim == 1:
        t = t.shape(1, t.size)
        y = y.shape(1, y.size)
        
    if t.size == y.size:
        t = t.argmax(axis = 1)
    batch_size = y.shape[0]
    return np.sum(np.log(y[np.arang(batch_size), t ])) / batch_size


def softmax_loss(x, t):
    y = softmax(x)
    return cross_entropy_error(y, t)


def num_grad(f, x):
    h = 1e-4
    grad = np.zeros_like(x) 
    it = np.nditer(x, flages=["multi_index"], op_flages = ["readwrite"])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)
        
        x[idx] = tmp_val - h
        fxh2 = f(x)
        grad[idx] = (fxh1 - fxh2) / (2 * h)
        
        x[idx] = tmp_val
        it.iternext()
    return grad

class sigmoid:
    def __init__(self):
        self.out = None
    
    def forward(self, x):
        out = sigmoid(x)
        self.out = out
        return out
    
    def backward(self, dout):
        dx = dout * (1.0 - self.out ) * self.out
        
        return dx
    
    
class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.original_x_shape = None
        self.dW = None
        self.db = None
    
    def forward(self, x):
        self.original_x_shape = x.shape
        x = x.reshape(x.shape[0], -1)
        self.x = x
        out = np.dot(self.x, self.W) + self.b
        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)
        dx = dx.reshape(*self.original_x_shape)

        return dx

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None
        
    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        
        return self.loss

    def backward(self, dout = 1):
        batch_size = self.t.shape[0]
        if self.t.size == self.y.size:
            dx = (self.y - self.t) / batch_size
        else:
            dx = self.y.copy()
            dx[np.arange(batch_size), self.t] -= 1
            dx = dx / batch_size
        
        return dx
        
        
    
    
class Relu:
    def __init__(self):
        self.mask = None
        
    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask]= 0
        
        return out
    
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        
        return dx

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std = 0.01):
        self.params = {}
        self.params["W1"] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params["b1"] = np.zeros(hidden_size)
        self.params["W1"] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params["b2"] = np.zeros(output_size)
        
        # 계층 생성
        self.layers = OrderedDict()
        self.layers["Affine1"] = Affine(self.params["W1"], self.params["b1"])
        self.layers["Relu1"] = Relu()
        self.layers["Affine2"] = Affine(self.params["W2"], self.params["b2"])
        self.lastLayer = SoftmaxWithLoss()
        
    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)
      
        
        return x
    
    def loss(self, x, t):
        y = self.predict(x)
        
        return self.lastLayer.forward(x, t)
    
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis = 1)
        if t.ndim != 1:
            t = np.argmax(t, axis = 1)
        
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy


    def numerical_gradient(self, x, t):
        loss_w = lambda w: self.loss(x, t)
        
        grads = {}
        grads["W1"] = num_grad(loss_w, self.params["W1"])
        grads["b1"] = num_grad(loss_w, self.params["b1"])
        grads["W2"] = num_grad(loss_w, self.params["W2"])
        grads["b2"] = num_grad(loss_w, self.params["b2"])
        
        
        return grads
        

    def gradient(self, x, t):
        
        self.loss(x, t)
        
        dout = 1
        dout = self.lastLayer.backward(dout)
        
        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)
        
        grads = {}
        grads['W1'] = self.layers['Affine1'].dW
        grads['b1'] = self.layers['Affine1'].db
        grads['W2'] = self.layers['Affine2'].dW
        grads['b2'] = self.layers['Affine2'].db


        return grads
    