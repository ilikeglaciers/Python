inputs = [1,2,3,2.5]
weights1 = [0.1,0.2,0.3,0.25]
weights2 = [0.5,-0.9,0.7,0.2]
weights3 = [0.1,-0.4,0.7,0.6]
bias1= 3.0
bias2 = 4.0
bias3 = 2.3
neuron1 = (inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3])+bias1
neuron2 = (inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3])+bias2
neuron3 = (inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3])+bias3
outputs = [neuron1,neuron2, neuron3 ]
print(outputs)
