import sim_data
from dnn1 import DNN1

x_data, y_data = sim_data.load_data()

model = DNN1(2, 10, 3)

model.fit(x_data,y_data, epochs=1000, verbose=0)
loss, accuracy = model.evaluate(x_data, y_data, batch_size=100)

print(loss, accuracy)