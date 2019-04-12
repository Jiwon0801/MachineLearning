from keras.models import Model
from keras.layers import Input, Dense, Activation

class SNN2(Model): 
    def __init__(self, num_input, num_output):

        x = Input(shape = (num_input,))
        output = Dense(num_output)
        softmax = Activation('softmax')

        y = softmax(output(x))
        
        super().__init__(x, y)
        
        self.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])