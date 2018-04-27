import numpy as np;
Input = np.array([0.1, 0.2, 0.7]);
Wij = np.array(([0.1, 0.2, 0.3], [0.3, 0.2, 0.7], [0.4, 0.3, 0.9]));
Wjk = np.array(([0.2, 0.3, 0.5], [0.3, 0.5, 0.7], [0.6, 0.4, 0.8]));
Wkl = np.array(([0.1, 0.4, 0.8], [0.3, 0.7, 0.2], [0.5, 0.2, 0.9]));

Wk1l = Wkl[0];
Wk1l1 = Wk1l[0];
Wk1l2 = Wk1l[1];
Wk1l3 = Wk1l[2];
print(Wk1l1, Wk1l2, Wk1l3);
Wk2l = Wkl[1];
Wk2l1 = Wk2l[0];
Wk2l2 = Wk2l[1];
Wk2l3 = Wk2l[2];
print(Wk2l1, Wk2l2, Wk2l3);
Wk3l = Wkl[2];
Wk3l1 = Wk3l[0];
Wk3l2 = Wk3l[1];
Wk3l3 = Wk3l[2];
print(Wk3l1, Wk3l2, Wk3l3);
Output = np.array([1.0, 0.0, 0.0]);
b = np.array([1.0, 1.0, 1.0]);
n = 0.01;
h1in = np.dot(Input, Wij) + b;
h1out = np.maximum(0, h1in);
h2in = np.dot(h1out, Wjk) + b;
h2out = 1/(1+np.exp(-h2in));
Oin = np.dot(h2out, Wkl) +b;
Oin1 = Oin[0];
Oin2 = Oin[1];
Oin3 = Oin[2];

Oout = (np.exp(Oin)/np.sum(np.exp(Oin))); 
Error = -1*np.sum((Output*np.log(Oout))+((1-Output)*np.log(1-Oout)));
dEdhOout = (-1*((Output*(1/Oout)+ (1-Output)*(1/(1-Oout)))));
dEdhOout1 = dEdhOout[0];
dEdhOout2 = dEdhOout[1];
dEdhOout3 = dEdhOout[2];

dOoutdOin1 = np.exp(Oin1)*(np.exp(Oin2)+np.exp(Oin3))/((np.sum(np.exp(Oin)))**2);
dOoutdOin2 = np.exp(Oin2)*(np.exp(Oin1)+np.exp(Oin3))/((np.sum(np.exp(Oin)))**2);
dOoutdOin3 = np.exp(Oin3)*(np.exp(Oin1)+np.exp(Oin2))/((np.sum(np.exp(Oin)))**2);

dOoutdOin = np.array([dOoutdOin1, dOoutdOin2, dOoutdOin3]);

dOindkl1 = h2out;
dOindk1l1 = dOindkl1[0];
dOindk2l1 = dOindkl1[1];
dOindk3l1 = dOindkl1[2];

dOindkl2 = h2out;
dOindk1l2 = dOindkl1[0];
dOindk2l2 = dOindkl1[1];
dOindk3l2 = dOindkl1[2];

dOindkl3 = h2out;
dOindk1l3 = dOindkl1[0];
dOindk2l3 = dOindkl1[1];
dOindk3l3 = dOindkl1[2];

deltaWkl = np.array(([dEdhOout1*dOoutdOin1*dOindk1l1, dEdhOout2*dOoutdOin2*dOindk1l2, dEdhOout3*dOoutdOin3*dOindk1l3],
                    [dEdhOout1*dOoutdOin1*dOindk2l1, dEdhOout2*dOoutdOin2*dOindk2l2, dEdhOout3*dOoutdOin3*dOindk2l3],
                    [dEdhOout1*dOoutdOin1*dOindk3l1, dEdhOout2*dOoutdOin2*dOindk3l2, dEdhOout3*dOoutdOin3*dOindk3l3]));
Wklprime = Wkl - (n*deltaWkl); 

dh2outdh2in = (h2out*(1-h2out));
# dEdh2out1 = dEdhOout*                   
# print(Wk1l1);   











