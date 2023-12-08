import numpy as np
import sys
import os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from utils import TwoLayerNet

import matplotlib.pyplot as plt     # 추가 분
import pickle                       # 추가 분


(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=False)

iters_num = 10000  # 반복횟수  ==> 변경 10000번으로

train_size = x_train.shape[0]

batch_size = 100  # 미니배치 크기
learning_rate = 0.1   
 
network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

train_loss_list = []          
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)
print("iter_per_epoch = ",iter_per_epoch)


for i in range(iters_num):
    #print(i, " 번째")
    # 미니배치 획득
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    # 기울기 계산
    #grad = network.numerical_gradient(x_batch, t_batch)
    grad = network.gradient(x_batch, t_batch)  # 추가 분 : 이것으로 바꿔야함

    # 매개변수 갱신
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]

    # 학습 경과 기록
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    # 1에폭 당 정확도 계산 ==> 추가 분 : 이 부분을 살려야함
    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print("train acc, test acc | "
              + str(train_acc) + ", " + str(test_acc))



#print("train loss list : ", train_acc_list)     # 기능 막기

x = np.arange(iters_num)           # 추가 분 : x축을 그리기 위함
plt.plot(x, train_loss_list)       # 추가 분 : 훈련 오차가 줄어드는것 그래프로 그림

plt.show()                         # 추가 분

with open("my_params.pkl", "wb") as file:   # 추가 분 : 본인이 생성한 것 저장
    pickle.dump(network.params, file)
    
epo = np.arange(len(train_acc_list))        # 추가 분 : 검출률 그리기 위함
plt.plot(epo, train_acc_list)               # 추가 분
plt.show()                                  # 추가 분