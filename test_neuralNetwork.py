from neural_network import neuralNetwork # if * all def and classes can use





n = neuralNetwork(3,3,3,0.3)

print(n.wih)
print(n.who)

print(n.query([1.0,0.5,-1.5]))

data_file = open("mnist_dataset/mnist_train_100.csv","r")
data_list = data_file.readlines()
data_file.close()

#print(len(data_list))
#print(data_list[2])

#n.GenerateMapShow(data_list[2])
print(n.NormalizeBetweenZeroAndOne(data_list[2]))
