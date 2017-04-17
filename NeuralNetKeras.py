from keras.models import Sequential
from keras.layers import Dense
import numpy


dataset = numpy.loadtxt("D:\Machine Learning - Stanford\machineLearning\Skin_NonSkin.txt", delimiter="\t")

#training dataset
X = dataset[50000:,0:3]
Y = dataset[50000:,3]

#testing dataset
XT=dataset[1:50000,0:3]
YT=dataset[1:50000,3]


# create model
model = Sequential()
model.add(Dense(12, input_dim=3, init='uniform', activation='relu'))
model.add(Dense(3, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X, Y, nb_epoch=10, batch_size=100)


# evaluate the model
scores = model.evaluate(XT, YT)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))



# Gives 100% accuracy in 3 epochs and takes 6 minutes to run on an i7 2.6 GHz processor with 8 Gb RAM.
