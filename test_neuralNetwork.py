from neural_network import neuralNetwork # if * all def and classes can use





#n = neuralNetwork(3,3,3,0.3)

#print(n.wih)
#print(n.who)

#print(n.query([1.0,0.5,-1.5]))

training_data_file = open("mnist_dataset/mnist_train.csv","r")
training_data_list = training_data_file.readlines()
training_data_file.close()


#n.GenerateMapShow(data_list[1])
#print(n.NormalizeBetweenZeroAndOne(data_list[2]))

input_nodes = 784
hidden_nodes = 200
output_nodes = 10
learning_rate = 0.1

epoche = 7 # multi times to train

n = neuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)

for e in range(epoche):
    for record in training_data_list:
        label = record.split(',')[0]
        inputs = n.NormalizeBetweenZeroAndOne(record) # 1: means from 1 to end
        targets  = n.targets(label)
        n.train(inputs,targets)
        pass
pass


test_data_file = open("mnist_dataset/mnist_test.csv","r")
test_data_list = test_data_file.readlines()
test_data_file.close()

#n.GenerateMapShow(test_data_list[8])


scoredcard = []

for record in test_data_list:
    all_values = record.split(',')
    current_label = int(all_values[0])
    #print(f"Current Label : {current_label}")
    inputs = n.NormalizeBetweenZeroAndOne(record) # 1: means from 1 to end
    outputs = n.query(inputs)
    label = n.getArgMax(outputs)
    #print(f"Networks awnser : {label}")
    if (label == current_label):
        scoredcard.append(1)
    else:
        scoredcard.append(0)
        pass
    pass

#print(scoredcard)
print(f"performance :{n.performance(scoredcard)}")