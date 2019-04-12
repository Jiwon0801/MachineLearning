from keras.models import Sequential
from keras.layers import Input, Dense, Activation

class DNN(Sequential):
    def __init__(self, num_input, num_hidde, nnum_output):
        super().__init__()

        self.add(Dense(num_hidde[0], activation='relu', input_shape=(num_input,)))
        self.add(Dense(num_hidde[1], activation='relu'))
        self.add(Dense(nnum_output, activation='softmax'))
        
        self.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])