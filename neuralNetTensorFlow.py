# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:49:07 2017

@author: Ketakee Nimavat
"""

import tensorflow as tf
import numpy as np
import sys
import os

dataset = np.loadtxt("Enter\Path\Skin_NonSkin.txt", delimiter="\t")
# split into input (X) and output (Y) variables
X1= dataset[:,0:3]
Y1 = dataset[:,3]
print(len(X1))
X=tf.cast(X1,tf.float32)
Y=tf.cast(Y1,tf.float32)
print(X)

#number of nodes in the hidden layers
nhl1=3
nhl2=3
nhl3=2

#number of classes
n_classes=2
batch_size=100

x=tf.placeholder('float32',[None,3])
y=tf.placeholder('float32',[None,1])

def neural_net(data):
   
        hidden_1_layer={'Weights':tf.Variable(tf.random_normal([3,nhl1])),'biases': tf.Variable(tf.random_normal([nhl1]))}
        hidden_2_layer={'Weights':tf.Variable(tf.random_normal([nhl1,nhl2])),'biases': tf.Variable(tf.random_normal([nhl2]))}
        hidden_3_layer={'Weights':tf.Variable(tf.random_normal([nhl2,nhl3])),'biases': tf.Variable(tf.random_normal([nhl3]))}
        output_layer={'Weights':tf.Variable(tf.random_normal([nhl3,n_classes])),'biases': tf.Variable(tf.random_normal([n_classes]))}
                                                               
        l1=tf.add(tf.matmul(data, hidden_1_layer['Weights']), hidden_1_layer['biases'])
        l1=tf.nn.relu(l1)
        
        l2=tf.add(tf.matmul(l1, hidden_2_layer['Weights']), hidden_2_layer['biases'])
        l2=tf.nn.relu(l2)
        
        l3=tf.add(tf.matmul(l2, hidden_3_layer['Weights']), hidden_3_layer['biases'])
        l2=tf.nn.relu(l3)
        
        output=tf.matmul(l3, output_layer['Weights'])+ output_layer['biases']
        return output
    
def train_neural_network(x):
      
        prediction=neural_net(x)
        print(prediction)
        cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y) )
        optimizer = tf.train.AdamOptimizer().minimize(cost)

        hm_epochs=10
        sess = tf.Session()

        with sess.as_default():
                try:

                    sess.run(tf.global_variables_initializer())
                    for epoch in range(hm_epochs):
                        epoch_loss=0
                        #no of iterations
                        i=0
                        while i<245057:
                            start=i
                            end=i+batch_size
                            batch_x=np.array(X1[start:end])
                            batch_y=np.array(Y1[start:end])
                            print(batch_x)
                            print(batch_y)
                            _, c= sess.run([cost,optimizer],feed_dict={x:batch_x,y:batch_y})
                            epoch_loss = epoch_loss + c
                        i+=batch_size
                        print('Epoch ',epoch, ' completed out of :',hm_epochs,"  loss: ", epoch_loss)
                except:
                        print("exception",sys.exc_info() )
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(exc_type, fname, exc_tb.tb_lineno)
                correct=tf.equal(tf.argmax(prediction,1),tf.argmax(y,1))
                accuracy=tf.reduce_mean(tf.cast(correct,'float'))
                try:
                    print('Accuracy', accuracy.eval(feed_dict={x:X1,y:Y1}))
                except:
                    print("Accuracy")
                    print(sys.exc_info())

train_neural_network(X)
