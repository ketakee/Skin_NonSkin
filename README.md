# Skin_NonSkin

Contains python code for classification of colours as skin or nonskin.
There are three ways it has been attempted:
  1. Keras
  2. Azure machine learning studio
  3. TensorFlow (contains errors.)
  
  
  The Keras version uses the Adam optimizer.
  
  
  A neural network on the azure studio gives 99.9% accuracy. It is deployed as a service in "AzureService.py"
  
  
  
  The tensorflow code is based on the mnsit training example. 
  It has some errors which need to be resolved.
  They're about data formats being different when sess.run() is called. 
  
  The dataset can be obtained from here:
  https://archive.ics.uci.edu/ml/datasets/Skin+Segmentation
  
  
  
  
