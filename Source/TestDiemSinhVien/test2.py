import numpy as np;
from numpy import dtype;
 
# X = (hours studying, hours sleeping), y = score on test, xPredicted = 4 hours studying & 8 hours sleeping (input data for prediction)
X = np.array(([9, 9, 10, 9.5], [2, 1, 0, 0]), dtype = float);
y = np.array(([1], [0]), dtype = float); #maximum of X array
xPredicted = np.array(([2, 1, 0, 0]), dtype = float); #max test score is 100
 
# # scale units 
X = X/np.amax(X, axis = 0)  
xPredicted = xPredicted/np.amax(xPredicted, axis = 0);
y = y/np.amax(y, axis = 0)
print(X);
class Neural_Network(object):
    def __init__(self):
        #parameter
        self.inputSize = 4;
        self.outputSize = 4;
        self.hiddenSize =4;
         
        #weights
        self.W1 = np.random.rand(self.inputSize, self.hiddenSize); 
        self.W2 = np.random.rand(self.hiddenSize, self.outputSize);
     
    def forward(self, X):
 
        self.z = np.dot(X, self.W1); 
        self.z2 = self.sigmoid(self.z);
        self.z3 = np.dot(self.z2, self.W2); 
        o = self.sigmoid(self.z3);  
        return o;
     
    def sigmoid(self, s):
        return 1/(1+np.exp(-s));
     
    def sigmoidPrime(self, s):
 
        return s * (1 - s);
    def backward(self, X, y, o):
 
        self.o_error = y - o;# error in output
        self.o_delta = self.o_error*self.sigmoidPrime(o);# applying derivative of sigmoid to error
        self.z2_error = self.o_delta.dot(self.W2.T); # z2 error: how much our hidden layer weights contributed to output error
        self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2);# applying derivative of sigmoid to z2 error
        self.W1 += X.T.dot(self.z2_delta);# adjusting first set (input --> hidden) weights
        self.W2 += self.z2.T.dot(self.o_delta);# adjusting second set (hidden --> output) weights
     
    def train(self, X, y):
        o = self.forward(X);
        self.backward(X, y, o);
         
    def saveWeights(self):
        np.savetxt("w1.txt", self.W1, fmt="%s");
        np.savetxt("w2.txt", self.W2, fmt="%s");
         
    def predict(self):
        print("Predicted data based on trained weighs:");
        print("Input (scaled): \n" + str(xPredicted));
        print("Output: \n" + str(self.forward(xPredicted)));    
         
NN = Neural_Network();
for i in xrange(100): # trains the NN 10,000 times
    print("#" + str(i) + "\n");
    print("Input (scaled): \n" + str(X));
    print("Actual Output: \n" + str(y));
    print("Predicted Output: \n" + str(NN.forward(X)));
    print("Loss: \n" + str(np.mean(np.square(y-NN.forward(X))))); # mean sum squared loss
    print("\n");
    NN.train(X, y)
NN.saveWeights();
NN.predict();       
     
     