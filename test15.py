import numpy as np;

Input = np.array([0.4, 0.6]);
Wik = np.array(([0.2, 0.3], [0.6, 0.4]), dtype = float);
b = np.array(([1.0,1.0]), dtype = float);
Output = np.array(([1.0, 0.0]), dtype = float);
h2in = np.dot(Input, Wik) + b;
h2out = 1/(1+np.exp(-h2in));
Error = -1*np.sum((Output*np.log(h2out))+((1-Output)*np.log(1-h2out)));

dEdh2out = (-1*((Output*(1/h2out)+ (1-Output)*(1/(1-h2out)))));
dEdh2out1 = dEdh2out[0];
dEdh2out2 = dEdh2out[1];

dh2outdh2in = (h2out*(1-h2out));
dh2outdh2in1 = dh2outdh2in[0];
dh2outdh2in2 = dh2outdh2in[1];

dh2indwik1 = Input;
dh2indwi1k1 = dh2indwik1[0];
dh2indwi2k1 = dh2indwik1[1];
        
dh2indwik2 = Input;
dh2indwi1k2 = dh2indwik2[0];
dh2indwi2k2 = dh2indwik2[1];

deltaW1k1 = dEdh2out1*dh2outdh2in1*dh2indwi1k1;
deltaW2k1 = dEdh2out1*dh2outdh2in1*dh2indwi2k1;
deltaW1k2 = dEdh2out2*dh2outdh2in2*dh2indwi1k2;
deltaW2k2 = dEdh2out2*dh2outdh2in2*dh2indwi2k2;

deltaWik = np.array(([deltaW1k1, deltaW1k2], [deltaW2k1, deltaW2k2]));

lr = 0.01;
Wikprime = Wik - (lr*deltaWik);
print(Wikprime);
