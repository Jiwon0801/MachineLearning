from keras.models import Sequential
from keras.layers import Input, Dense, Activation

class SNN1(Sequential):
    def __init__(self, num_input, num_output):
        super().__init__()
        
        self.add(Dense(num_output, input_shape=(num_input,), activation='softmax'))
        
        self.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])