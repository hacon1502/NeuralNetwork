import numpy as np

f1 = open('E:/CoreJava/TestJava/src/vmio/input1.txt', 'r+');
data1 = f1.read();
f1.close();
data1 = data1.split();
x = np.array([data1], dtype=np.float);
X = np.reshape(x, (200000, 2));

f2 = open('E:/CoreJava/TestJava/src/vmio/output1.txt', 'r+');
data2 = f2.read();
f2.close();
data2 = data2.split();
y = np.array([data2], dtype=np.float);
y = np.reshape(y, (200000,1));
  
xPredicted = np.array(([0.7, 0.3]), dtype = np.float);
 
X = X/np.amax(X, axis = 0);
y = y/np.amax(y, axis = 0);
xPredicted = xPredicted/np.amax(xPredicted, axis = 0);
class Neural_Network(object):
    def __init__(self):
        #parameter
        self.inputSize = 2;
        self.outputSize = 2;
        self.hiddenSize =2;
          
        #weights
        self.W1 = np.random.rand(self.inputSize, self.hiddenSize); 
        self.W2 = np.random.rand(self.hiddenSize, self.outputSize);
    def forward(self, Xp):
        #forward propagation through our network
        self.z2 = np.dot(Xp, self.W1); 
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
     
    def backward(self, Xp, yp):
        self.yHat = self.forward(Xp);
#         error = yp - self.yHat;
#         print(erorr);
        self.delta3 = np.multiply(-(yp - self.yHat), self.sigmoidPrime(self.z3));    
        self.delta2 = np.dot(self.delta3, self.W2.T)*self.sigmoidPrime(self.z2);
        self.W2 += self.a2.T.dot(self.delta3);
        self.W1 += Xp.T.dot(self.delta2);
    def train(self, Xp, yp):
        self.yHat = self.forward(Xp);
        self.backward(Xp, yp);
          
    def saveWeights(self):
        np.savetxt("w1.txt", self.W1, fmt="%s");
        np.savetxt("w2.txt", self.W2, fmt="%s");
          
    def predict(self):
        print("Predicted data based on trained weighs:");
        print("Input (scaled): \n" + str(xPredicted));
        print("Output: \n" + str(self.forward(xPredicted)));    
          
NN = Neural_Network();
for i in range(0,200000):
    Xp = X[i];
    yp = y[i];
    NN.train(Xp, yp);
    NN.predict();
       
