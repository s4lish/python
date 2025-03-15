import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import os
import json
class neuralNetwork:
    
    def __init__(self,inputNodes,hiddenNodes,outputNodes,learningRate):
        self.iNodes = inputNodes
        self.hNodes = hiddenNodes
        self.oNodes = outputNodes
        
        self.lr = learningRate
        
        self.activation_function = lambda x: scipy.special.expit(x)
        
        #print(np.random.rand(3,3) - 0.5) # generate random num between 0 and 1 and put them on matrix (array 2D)
        #save in files becase after each run then dont want to change them.
        filename = "ws.txt"
        if not os.path.exists(filename) or os.stat(filename).st_size == 0:
            self.wih = np.round(np.random.rand(self.hNodes,self.iNodes) - 0.5,4)
            self.who = np.round(np.random.rand(self.oNodes,self.hNodes) - 0.5,4)
            with open(filename, "w") as f:
                json.dump({"wih": self.wih.tolist(), "who": self.who.tolist()}, f)           
            print("Generated and saved random weights.")
        else:
            with open(filename,"r") as f:
                data = json.load(f)
                self.wih = np.array(data["wih"])
                self.who = np.array(data["who"])
            print("Loaded weights from file.")

            
        pass
    
    def train(self,inputs_list,targets_list):
        
        inputs = np.array(inputs_list,ndmin=2).T
        targets = np.array(targets_list,ndmin=2).T
        hidden_inputs = np.dot(self.wih,inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = np.dot(self.who,hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        
        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.who.T,output_errors)
        
        self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)),np.transpose(hidden_outputs))
        
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),np.transpose(inputs))
        
        
        pass
    
    
    
    def query(self,inputs_list):
        #convert inputs list to 2d array
        inputs = np.array(inputs_list,ndmin=2).T
        
        hidden_inputs = np.dot(self.wih,inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        
        final_inputs = np.dot(self.who,hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        
        return final_outputs

    
    def GenerateMapShow(self,data_list):
        all_values = data_list.split(",")
        image_array = np.asarray(all_values[1:], dtype=float).reshape((28,28)) # all_values[1:] all values except first one. start from 1 to end and not Index 0
        plt.imshow(image_array, cmap='Greys', interpolation='None')
        plt.show()
        pass
    
    
    def NormalizeBetweenZeroAndOne(self,data_list):
        all_values = data_list.split(",")
        scaled_input = (np.asarray(all_values[1:],dtype=float) / 255.0 * 0.99) + 0.01 # all_values[1:] all values except first one. start from 1 to end and not Index 0
        return scaled_input

        
        
        
        
    pass