import numpy as np

# X = (hours sleeping, hours studying), y = Score on test
X = np.array(([3,5], [5,1], [10,2]), dtype=float).T
print(X);
y = np.array(([75], [82], [93]), dtype=float)
xPredicted = np.array(([4,8]), dtype = float);
# Normalize
X = X/np.amax(X, axis=0)
y = y/100 #Max test score is 100
xPredicted = xPredicted/np.amax(xPredicted, axis = 0);
## ----------------------- Part 4 ---------------------------- ##
 
# Whole Class with additions:
class Neural_Network(object):
    def __init__(self):        
        #Define Hyperparameters
        self.inputLayerSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 3
         
        #Weights (parameters)
        self.W1 = np.random.randn(self.inputLayerSize,self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize,self.outputLayerSize)
         
    def forward(self, X):
        #Propagate inputs through network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3) 
        return yHat
         
    def sigmoid(self, z):
        #Apply sigmoid activation function to scalar, vector, or matrix
        return 1/(1+np.exp(-z))
     
    def sigmoidPrime(self,z):
        #Gradient of sigmoid
        return np.exp(-z)/((1+np.exp(-z))**2)
     
    def costFunction(self, X, y):
        #Compute cost for given X,y, use weights already stored in class.
        self.yHat = self.forward(X)
        J = 0.5*sum((y-self.yHat)**2)
        return J
         
    def costFunctionPrime(self, X, y):
        #Compute derivative with respect to W and W2 for a given X and y:
        self.yHat = self.forward(X)
         
        delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)
         
        delta2 = np.dot(delta3, self.W2.T)*self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(X.T, delta2)  
         
        return dJdW1, dJdW2
    def train(self, X, y):
        self.o = self.forward(X);
        self.costFunctionPrime(X, y);
         
    def saveWeights(self):
        np.savetxt("w1.txt", self.W1, fmt="%s");
        np.savetxt("w2.txt", self.W2, fmt="%s");
         
    def predict(self):
        print("Predicted data based on trained weighs:");
        print("Input (scaled): \n" + str(xPredicted));
        print("Output: \n" + str(self.forward(xPredicted)));    
         
NN = Neural_Network();
for i in xrange(1000): # trains the NN 10,000 times
    print("#" + str(i) + "\n");
    print("Input (scaled): \n" + str(X));
    print("Actual Output: \n" + str(y));
    print("Predicted Output: \n" + str(NN.forward(X)));
    print("Loss: \n" + str(np.mean(np.square(y-NN.forward(X))))); # mean sum squared loss
    print("\n");
    NN.train(X, y)
NN.saveWeights();
NN.predict();       
     