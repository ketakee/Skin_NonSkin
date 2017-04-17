# Skin_NonSkin

Contains python code for classification of colours as skin or nonskin.
The dataset can be obtained from here:
  https://archive.ics.uci.edu/ml/datasets/Skin+Segmentation
  
  
  
There are three ways it has been attempted:
  1. Keras
  2. Azure machine learning studio
  3. TensorFlow 
  
  
  Two of these ways resolve the classification,the tensorflow code however, has some errors.
 
 1. Keras
 
  UPDATE:The previous version of this claimed the accuracy was 52% after 3 epochs, but it turns out there was a logical error in the code
  where I had changed the labels from (1,2) to (1,0) for the training data. 
  
  This change was not made in the testing data and was causing the accuracy to reduce substantially. After fixing that,
  the keras code works great with 100% accuracy in three epochs.
 
 2. Azure machine learning studio
 
   A neural network made using the azure studio gives 99.9% accuracy. It is deployed as a service in "AzureService.py"
  
 3. Tensorflow
 
  The tensorflow code is based on the mnsit training example. 
  It has some errors about data formats being different when sess.run() is called, these errors need to be resolved. 
  
  
  
  
  
  
