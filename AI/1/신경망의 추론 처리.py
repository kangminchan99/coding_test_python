import sys, os
sys.path.append('/Users/minchan/Documents/GitHub/coding_test_python/AI/1/dataset')
from dataset.mnist import load_mnist
import pickle

def set_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False, one_hot_label=True)
    return x_test, t_test

def init_network():
    with open('/Users/minchan/Documents/GitHub/coding_test_python/AI/1/dataset/sample_weight.pkl', 'rb') as f :
        network = pickle.load(f)

        return network

# x, t = get_data()
net = init_network()
print(net['b1'])
