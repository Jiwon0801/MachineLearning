import sim_data
from snn import SNN1

x_data, y_data = sim_data.load_data()

model = SNN1(2,3)

model.fit(x_data, y_data, epochs=100, verbose=0)
loss, accuracy = model.evaluate(x_data, y_data, batch_size=100)

print(loss, accuracy)