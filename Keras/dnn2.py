from keras.models import Model
from keras.layers import Input, Dense, Activation

class DNN2(Model):
    def __init__(self, num_input, num_hidden, num_output):
        hidden = Dense(num_hidden)
        relu = Activation('relu')
        output = Dense(num_output)
        softmax = Activation('softmax')

        x = Input(shape=(num_input,))
        h = relu(hidden(x))
        y = softmax(output(h))

        super().__init__(x, y)

        self.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])