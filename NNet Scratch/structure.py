import numpy as np
import pandas as pd
import sys

from sympy import N


class X:
    weights: list()
    biases: list() = []
    neural_network: list()


def import_data():
    data = pd.read_csv(sys.path[0]+"\\iris.data")
    return data

def fillter_data():
    pass


def weights_biases(nnet):
    print(nnet)
    weights = [np.ones((nnet[i], nnet[i+1])) for i in range(len(nnet)-1)]
    biases = [np.ones(nnet[i]) for i in range(1, len(nnet))]

    return weights, biases


def matrix_mul(vector_a, vector_b):
    return np.matmul(vector_a, vector_b)


def activation_function(x):
    return 1/(1+pow(np.math.e, -x))


def forward_propagation(data, nnet):
    for layer in nnet.weights:
        data = activation_function(matrix_mul(data, nnet.weights)+nnet.biases)

    return data  # it is output actually


def cost_function():
    matrix_mul(output_pred, output)


def backward_propagation(X, y, theta, learning_rate=0.01, iterations=100):
    pass


def inputs(input_size, output_size):
    nnet = [input_size]
    no_of_layers = int(input("No of Layers -> "))
    for i in range(1,no_of_layers-1):
        nnet.append(int(input(str(i+1)+" -> ")))
    
    nnet.append(output_size)
    return nnet


if __name__ == "__main__":
    # data test vs train
    data = import_data()
    
    train_test_split = int(data.size*int(input("Enter percentage of train vs test ->"))/100)
    test_data, train_data = data.loc[0:train_test_split], data.loc[train_test_split:]

    # structure
    net1 = X()
    net1.neural_network = inputs(data.shape[1]-1, (pd.unique(data.iloc[:,-1])).size)
    net1.weights, net1.biases = weights_biases(net1.neural_network)
    
    #processing
    for data1 in test_data:
        input_data = data1.iloc[:-2]
        label = data1.iloc[-1]
        
        processing(input_data,label,net1)
    
    
def processing(test_data,net1):
    # forward propagation
    output = forward_propagation(test_data, net1)

    # backward propagation
    net1.weights, net1.biases = backward_propagation(
        net1.weights, net1.biases)
