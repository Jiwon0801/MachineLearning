import tensorflow as tf
import numpy as np

class MultiLinearRegression:
    def __init__(self, w, b, learning_rate, steps=2000):
        self.x_data = np.random.randn(2000,3)
        self.noise = np.random.randn(1,2000) * 0.1
        self.y_data = np.matmul(w, self.x_data.T) + b + self.noise

        self.x = tf.placeholder(tf.float32, shape = [None, 3])
        self.y_true = tf.placeholder(tf.float32, shape=None)
        self.w = tf.Variable([[0,0,0]], dtype=tf.float32)
        self.b = tf.Variable(0, dtype=tf.float32)
      
        self.y_pred = tf.matmul(w, tf.transpose(self.x)) + self.b       
        self.loss = tf.reduce_mean(tf.square(self.y_true-self.y_pred))

        self.optimizer = tf.train.GradientDescentOptimizer(learning_rate)
        self.train = self.optimizer.minimize(self.loss)

        self.init = tf.global_variables_initializer()


    def training(self, steps):
        with tf.Session() as sess :
            sess.run(self.init)
            for step in range(steps):
                sess.run(self.train, {self.x: self.x_data, self.y_true: self.y_data})
                if(step%5 == 0):
                    print(step, sess.run([self.w,self.b]))
                    
            print(10, sess.run([self.w,self.b]))


if __name__ == "__main__":
    w = [0.3, 0.5, 0.1]
    b = -0.2
    mlr = MultiLinearRegression(w, b, 0.5, 2000)
    mlr.training(10)







    