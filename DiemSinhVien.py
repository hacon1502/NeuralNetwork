import numpy as np;
#Du lieu dau vao
f1 = open('E:/CoreJava/TestJava/src/vmio/input.txt', 'r+');  
data1 = f1.read();
f1.close();
data1 = data1.split();
x = np.array([data1], dtype=np.float);
Input = np.reshape(x, (200000, 2));

#Du lieu dau ra
f2 = open('E:/CoreJava/TestJava/src/vmio/output.txt', 'r+');
data2 = f2.read();
f2.close();
data2 = data2.split();
y = np.array([data2], dtype=np.float);
Output = np.reshape(y, (200000, 2));

#Bias
b = np.array([1.0, 1.0], dtype = float);
xPredicted = np.array(([7.0, 3.0]), dtype = np.float);
Input = Input/np.amax(Input, axis = 0);
Output = Output/np.amax(Output, axis = 0);
xPredicted = xPredicted/np.amax(xPredicted, axis = 0);
lr = 0.01;
class Neural_Network(object):
    #Mo hinh mang neural network 2x2
    def __init__(self):
        self.inputSize = 2;
        self.outputSize = 2;
        self.Wik = np.random.rand(self.inputSize, self.outputSize);
    
    # Foword Propagation 
    def forward(self, inp):
        self.h2in = np.dot(inp, self.Wik) + b;
        h2out = self.sigmoid(self.h2in);
        print("foward h2in:");
        print(self.h2in);
        print("foward h2out:"); 
        print(h2out);
        return h2out;
    
    # Ham sigmoid    
    def sigmoid(self, z):
        return 1.0/(1.0+np.exp(-z));
    
    # Dao ham sigmoid     
    def sigmoid_prime(self, z):
        return np.exp(-z)/((1+np.exp(-z))**2);    
    
    #Backpropagation   
    def backpropagation(self, inp, outp):
        self.h2out = self.forward(inp);
        #Error
        Error = (-1)*np.sum((outp*np.log(self.h2out))+((1-outp)*np.log(1-self.h2out)));
        
        #Tim trong so
        #dE/dwik = dE/dh2out * dh2out/dh2in * dh2in/dwik
        #dEdh2out
        dEdh2out = -1*((outp*(1/self.h2out)+ (1-outp)*(1/(1-self.h2out))));
        dEdh2out1 = dEdh2out[0];
        dEdh2out2 = dEdh2out[1];
        
        #dh2out/dh2in
        dh2outdh2in = (self.h2out*(1-self.h2out ));
        dh2outdh2in1 = dh2outdh2in[0];
        dh2outdh2in2 = dh2outdh2in[1];
        
        #dh2in/dwik
        dh2indwik1 = inp;
        dh2indwi1k1 = dh2indwik1[0];
        dh2indwi2k1 = dh2indwik1[1];
        
        dh2indwik2 = inp;
        dh2indwi1k2 = dh2indwik2[0];
        dh2indwi2k2 = dh2indwik2[1];
        
        #deltaWik
        deltaW1k1 = dEdh2out1*dh2outdh2in1*dh2indwi1k1;
        deltaW2k1 = dEdh2out1*dh2outdh2in1*dh2indwi2k1;
        deltaW1k2 = dEdh2out2*dh2outdh2in2*dh2indwi1k2;
        deltaW2k2 = dEdh2out2*dh2outdh2in2*dh2indwi2k2;
        
        deltaWik = np.array(([deltaW1k1, deltaW1k2], [deltaW2k1, deltaW2k2]));
        
        #Tim ra trong so chinh xac nhat
        Wikprime = self.Wik - (lr*deltaWik);
        Wik = Wikprime;
        print("Error:");
        print(Error);
        print("Wik:")
        print(Wik);
        return Wik, Error;
    #Train mang neural    
    def train(self, inp, outp):
        self.h2out = self.forward(inp);
        self.backpropagation(inp, outp);
    
    def saveWeights(self):
        np.savetxt("wik.txt", self.Wik, fmt="%s");
            
    def predict(self):
        print("Predicted data based on trained weighs:");
        print("Input (scaled): \n" + str(xPredicted));
        print("Output: \n" + str(self.forward(xPredicted)) +"\n");       

NN = Neural_Network();
#Train mang neural network den het do dai cua mang Input
for i in range(0,200000):
    print("# " + str(i));
    inp = Input[i];
    print("inp: " + str(inp));
    outp = Output[i];
    print("outp: " + str(outp));
    NN.backpropagation(inp, outp);
    NN.saveWeights();
NN.predict();
