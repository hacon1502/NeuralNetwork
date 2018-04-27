import numpy as np
from numpy import dtype
f1 = open('E:/CoreJava/TestJava/src/vmio/input.txt', 'r+');
data1 = f1.read();
f1.close();
data1 = data1.split();
x = np.array([data1], dtype=np.float);
X = np.reshape(x, (200000, 4));
 
f2 = open('E:/CoreJava/TestJava/src/vmio/output.txt', 'r+');
data2 = f2.read();
f2.close();
data2 = data2.split();
y = np.array([data2], dtype=np.float);
y = np.reshape(y, (200000,1));
 
xPredicted = np.array(([10.0, 10.0, 10.0, 10.0]), dtype = float);

X = X/np.amax(X, axis = 0);
y = y/4;
xPredicted = xPredicted/np.amax(xPredicted, axis = 0);
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
        #forward propagation through our network
        self.z2 = np.dot(X, self.W1); 
        self.a2 = self.sigmoid(self.z2);
        self.z3 = np.dot(self.a2, self.W2); 
        yHat = self.sigmoid(self.z3);  
        return yHat;
     
    def sigmoid(self, z):
        #Apply sigmoid activation function to scalar, vector, or matrix
        return 1/(1+np.exp(-z))
    
    def sigmoidPrime(self,z):
        #Gradient of sigmoid
        return np.exp(-z)/((1+np.exp(-z))**2)
    
    def backward(self, X, y, yHat):

        self.erorr = y - yHat;# error in output
        self.delta3 = np.multiply(-(y - yHat), self.sigmoidPrime(self.z3));    
        self.delta2 = np.dot(self.delta3, self.W2.T)*self.sigmoidPrime(self.z2);
        self.W2 += self.a2.T.dot(self.delta3);
        self.W1 += X.T.dot(self.delta2);
     
    def train(self, X, y):
        yHat = self.forward(X);
        self.backward(X, y, yHat);
         
    def saveWeights(self):
        np.savetxt("w1.txt", self.W1, fmt="%s");
        np.savetxt("w2.txt", self.W2, fmt="%s");
         
    def predict(self):
        print("Predicted data based on trained weighs:");
        print("Input (scaled): \n" + str(xPredicted));
        print("Output: \n" + str(self.forward(xPredicted)));    
         
NN = Neural_Network();
for i in xrange(10): # trains the NN 10,000 times
    print("#" + str(i) + "\n");
    print("Input (scaled): \n" + str(X));
    print("Actual Output: \n" + str(y));
    print("Predicted Output: \n" + str(NN.forward(X)));
    print("Loss: \n" + str(np.mean(np.square(y-NN.forward(X))))); # mean sum squared loss
    print("\n");
    NN.train(X, y)
NN.saveWeights();
NN.predict();       
     
