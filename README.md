# Skin_NonSkin

Contains python code for classification of colours as skin or nonskin.
The dataset can be obtained from here:
  https://archive.ics.uci.edu/ml/datasets/Skin+Segmentation
  
  
  
There are three ways it has been attempted:
  1. Keras
  2. Azure machine learning studio
  3. TensorFlow (contains errors.)
  
  
  Two of these ways resolve the classification, however the tensorflow code has some errors.
 
 1. Keras
 
  The Keras version uses the Adam optimizer.
  After 3 epochs, the accuracy is 35% and after 10 it is 52%.
  the accuracy should improve as the number of epochs are increased.
  It takes 60 minutes to train 2,00,000 data points with a btach size of 100.
  It gives a 99.97% accuracy on the training data.
 
 2. Azure machine learning studion
 
   A neural network made using the azure studio gives 99.9% accuracy. It is deployed as a service in "AzureService.py"
  
 3. Tensorflow
 
  The tensorflow code is based on the mnsit training example. 
  It has some errors which need to be resolved.
  They're about data formats being different when sess.run() is called. 
  
  
  
  
  
  
